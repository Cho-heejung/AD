import unittest

from action import Action

class TestAction(unittest.TestCase):

    def setUp(self):
        self.a = Action()
        # feeding
        self.meal = 30 # 단위 테스트에서 줄 밥 양 설정
        self.h = "■" * int((50 + 30) / 2.5) + str(50 + 30) + "%" # 단위 테스트 후 self.currentHunger 의 결과 = '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■80%'
        # washing
        self.washSubGauge = -10 # 단위 테스트에서 감소시킬 청결 수치 설정
        self.c = "■" * int((50 + (-10)) / 2.5) + str(50 + -(10)) + "%" # 단위 테스트 후 self.currentClean 의 결과 = '■■■■■■■■■■■■■■■■40%'
        # sleeping
        self.sleepAddGauge = -10 # 단위 테스트에서 증가시킬 졸음 수치 설정
        self.t = "■" * int((50 + 10) / 2.5) + str(50 + 10) + "%" # 단위 테스트 후 self.currentTired 의 결과 = '■■■■■■■■■■■■■■■■■■■■■■■■60%'
        # studying
        self.s1 = "■" * int((50 + 30) / 2.5) + str(50 + 30) + "%" # 단위 테스트 후 self.currentStress 의 결과 = '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■80%'
        # playing
        self.s2 = "■" * int((50 + (-15)) / 2.5) + str(50 + (-15)) + "%" # 단위 테스트 후 self.currentStress 의 결과 = '■■■■■■■■■■■■■■35%'

        self.notEqual = "■1%" # 모든 단위 테스트에서 assertNotEqual 을 확인할 gauge 상태 설정


    def tearDown(self): # 단위 테스트 종료 후
        pass # pass

    def testFeeding(self):
        self.assertEqual(self.a.feeding(self.meal), self.h)                         # 밥을 30 만큼 줬을 때 self.currentHunger 은 '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■80%' 이므로 self.h 와 equal
        self.assertNotEqual(self.a.feeding(self.meal), self.notEqual)               # 밥을 30 만큼 줬을 때 self.currentHunger 은 '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■80%' 이므로 '■1%' 과는 notEqual

    def testWashing(self):
        self.assertEqual(self.a.washing(self.washSubGauge), self.c)                 # 각 버튼을 한번 눌렀을 때 청결 수치가 10 감소하므로 self.currentClean 은 '■■■■■■■■■■■■■■■■40%' 이므로 self.c 와 equal
        self.assertNotEqual(self.a.washing(self.washSubGauge), self.notEqual)       # 각 버튼을 한번 눌렀을 때 청결 수치가 10 감소하므로 self.currentClean 은 '■■■■■■■■■■■■■■■■40%' 이므로  '■1%' 과는 notEqual

    def testSleeping(self):
        self.assertEqual(self.a.sleeping(self.sleepAddGauge), self.t)               # 각 버튼을 한번 눌렀을 때 졸음 수치가 10 증가하므로 self.currentTired 는 '■■■■■■■■■■■■■■■■■■■■■■■■60%' 이므로 self.t 와 equal
        self.assertNotEqual(self.a.sleeping(self.sleepAddGauge), self.notEqual)     # 각 버튼을 한번 눌렀을 때 졸음 수치가 10 증가하므로 self.currentTired 는 '■■■■■■■■■■■■■■■■■■■■■■■■60%' 이므로 '■1%' 과는 notEqual

    def testStudying(self):
        self.assertEqual(self.a.studying(), self.s1)              # 공부하기 버튼을 한번 눌렀을 때 스트레스 수치가 30 증가하므로 self.currentStress 는 '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■80%' 이므로 self.s1 과 equal
        self.assertNotEqual(self.a.studying(), self.notEqual)     # 공부하기 버튼을 한번 눌렀을 때 스트레스 수치가 30 증가하므로 self.currentStress 는 '■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■80%' 이므로 '■1%' 과는 notEqual

    def testPlaying(self):
        self.assertEqual(self.a.playing(), self.s2)                # 놀아주기 버튼을 한번 눌렀을 때 스트레스 수치가 15 감소하므로 self.currentStress 는 '■■■■■■■■■■■■■■35%' 이므로 self.s2 와 equal
        self.assertNotEqual(self.a.playing(), self.notEqual)       # 놀아주기 버튼을 한번 눌렀을 때 스트레스 수치가 15 감소하므로 self.currentStress 는 '■■■■■■■■■■■■■■35%' 이므로 '■1%' 과는 notEqual


if __name__ == '__main__':
    unittest.main()