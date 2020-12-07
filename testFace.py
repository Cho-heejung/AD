import unittest # unittest 모듈 import

from tamagotchi import Tamagotchi # 다마고치 모듈 import

class TestFace(unittest.TestCase): # 얼굴이 바뀌는 단위 테스트 클래스 생성

    def setUp(self): # 기본 값 세팅
        self.t = Tamagotchi()
        self.a1 = 50
        self.a2 = 20
        self.a3 = 80
        self.a4 = 100
        self.smile = "face_smile.png"
        self.sad = "face_sad.png"
        self.wink = "face_wink.png"
        self.kiss = "face_kiss.png"

    def tearDown(self): # 단위 테스트 종료 후
        pass # pass

    def testFaceChange(self):
        self.assertEqual(self.t.faceChange(self.a1), self.smile)        # all 게이지가 50일 때 다마고치의 표정은 smile 이므로 (smile == smile)
        self.assertNotEqual(self.t.faceChange(self.a2), self.smile)     # all 게이지가 20일 때 다마고치의 표정은 sad 이므로 (sad != smile)
        self.assertEqual(self.t.faceChange(self.a2), self.sad)          # all 게이지가 20일 때 다마고치의 표정은 sad 이므로 (sad == sad)
        self.assertEqual(self.t.faceChange(self.a3), self.wink)         # all 게이지가 80일 때 다마고치의 표정은 wink 이므로 (wink == wink)
        self.assertEqual(self.t.faceChange(self.a4), self.kiss)         # all 게이지가 100일 때 다마고치의 표정은 kiss 이므로 (kiss == kiss)
        self.assertNotEqual(self.t.faceChange(self.a2), self.wink)      # all 게이지가 100일 때 다마고치의 표정은 kiss 이므로 (kiss != kiss)

if __name__ == '__main__':
    unittest.main()