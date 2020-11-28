from PyQt5.QtWidgets import QMessageBox
class Action:

    def __init__(self):
        self.hunger = 50
        self.clean = 50
        self.tired = 50
        self.study_cnt = 0
        self.age = 1
        self.stress = 50
        self.all = 50
        self.endGame = False

        self.currentHunger = "■" * (self.hunger) + str(self.hunger) + "%"
        self.currentClean = "■" * (self.clean) + str(self.clean) + "%"
        self.currentTired = "■" * (self.tired) + str(self.tired) + "%"
        self.currentStress = "■" * (self.stress) + str(self.stress) + "%"
        self.currentAll = "■" * (self.all) + str(self.all) + "%"

    def feeding(self, food):
        if (self.hunger + food <= 100 and self.hunger + food >= 0):
            self.hunger += food
        else:
            self.endGame = True
        self.currentHunger = "■" * (self.hunger) + str(self.hunger) + "%"

        return self.currentHunger

    def washing(self, wash):
        if (self.clean + int(wash) < 0):
            self.endGame = True
        elif (self.clean + int(wash) >= 100):
            self.clean = 100
        else:
            self.clean += int(wash)
        self.currentClean = "■" * (self.clean) + str(self.clean) + "%"

        return self.currentClean

    def sleeping(self, sleep):
        if (self.tired - int(sleep) > 100):
            self.endGame = True
        elif (self.tired - int(sleep) <= 0):
            self.tired = 0
        else:
            self.tired -= int(sleep)
        self.currentTired = "■" * (self.tired) + str(self.tired) + "%"

        return self.currentTired

    def studying(self):
        self.study_cnt += 1  # 공부 횟수 카운팅

        # 스트레스 게이지바 업데이트
        if (self.stress + 30 > 100):
            self.endGame = True
        else:
            self.stress += 30
            self.currentStress = "■" * (self.stress) + str(self.stress) + "%"

        return self.currentStress

    def playing(self):
        if (self.stress - 15 <= 0):
            self.endGame = True
        else:
            self.stress -= 15
        self.currentStress = "■" * (self.stress) + str(self.stress) + "%"

        return self.currentStress

    def all_gauge(self):
        if ((self.hunger + self.clean < 60) or (self.tired + self.stress >= 140)):
            if (self.all - 10 <= 0):
                self.all = 0
            else:
                self.all -= 10
        if ((self.hunger + self.clean >= 140) or (self.tired + self.stress < 60)):
            if (self.all + 10 >= 100):
                self.all = 100
            else:
                self.all += 10
        self.currentAll = "■" * (self.all) + str(self.all) + "%"
        if (self.all < 0):
            self.endGame = True