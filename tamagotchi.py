import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

from action import Action

class Button(QToolButton):
    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Tamagotchi(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.hunger = 50
        self.clean = 50
        self.tired = 50
        self.study_cnt = 0
        self.age = 1
        self.stress = 50
        self.all = 50

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 200, 1340, 700)
        self.setWindowTitle('Tamagotchi')

        self.cleanButton = QPushButton('씻기기')
        self.cleanButton.clicked.connect(self.button_clicked)
        self.sleepButton = QPushButton('재우기')
        self.sleepButton.clicked.connect(self.button_clicked)
        self.playButton = QPushButton('놀아주기')
        self.playButton.clicked.connect(self.button_clicked)
        self.studyButton = QPushButton('공부시키기')
        self.studyButton.clicked.connect(self.button_clicked)

        self.vbox = QVBoxLayout()

        self.hbox0 = QHBoxLayout()
        self.hbox0.addWidget(QLabel('~지금은~'))
        self.status_text = QLineEdit()
        self.status_text.setReadOnly(True)
        self.hbox0.addWidget(self.status_text)
        self.hbox0.addStretch(1)

        self.age_label = QLabel('나이 : ', self)
        self.age_output = QLineEdit(self)
        self.age_output.setReadOnly(True)
        self.age_output.resize(30, 30)
        self.age_output.setText(str(self.age))
        self.hbox0.addWidget(self.age_label)
        self.hbox0.addWidget(self.age_output)
        self.hbox0.addStretch(1)

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(QLabel('다마고치'))
        self.character_text = QTextEdit()
        self.character_text.setReadOnly(True)
        self.hbox1.addWidget(self.character_text)

        self.hbox2 = QHBoxLayout()
        self.hbox2.addWidget(QLabel('밥 주 기 '))
        self.feed_edit = QLineEdit()
        self.hbox2.addWidget(self.feed_edit)
        self.feedButton = QPushButton('입력')
        self.feedButton.clicked.connect(self.button_clicked)
        self.hbox2.addWidget(self.feedButton)
        self.hbox2.addStretch(1)

        self.hbox2.addWidget(self.cleanButton)
        self.hbox2.addWidget(self.sleepButton)
        self.hbox2.addWidget(self.playButton)
        self.hbox2.addWidget(self.studyButton)

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(QLabel('종     합 '))
        self.all_text = QLineEdit()
        self.all_text.setReadOnly(True)
        self.hbox3.addWidget(self.all_text)
        self.all_text.setText("■" * (self.all) + str(self.all) + "%")

        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(QLabel('배 부 름 '))
        self.hunger_text = QLineEdit()
        self.hunger_text.setReadOnly(True)
        self.hbox4.addWidget(self.hunger_text)
        self.hunger_text.setText("■" * (self.hunger) + str(self.hunger) + "%")

        self.hbox5 = QHBoxLayout()
        self.hbox5.addWidget(QLabel('청     결 '))
        self.clean_text = QLineEdit()
        self.clean_text.setReadOnly(True)
        self.hbox5.addWidget(self.clean_text)
        self.clean_text.setText("■" * (self.clean) + str(self.clean) + "%")

        self.hbox6 = QHBoxLayout()
        self.hbox6.addWidget(QLabel('피     로 '))
        self.tired_text = QLineEdit()
        self.tired_text.setReadOnly(True)
        self.hbox6.addWidget(self.tired_text)
        self.tired_text.setText("■" * (self.tired) + str(self.tired) + "%")

        self.hbox7 = QHBoxLayout()
        self.hbox7.addWidget(QLabel('스트레스'))
        self.stress_text = QLineEdit()
        self.stress_text.setReadOnly(True)
        self.hbox7.addWidget(self.stress_text)
        self.stress_text.setText("■" * (self.stress) + str(self.stress) + "%")

        self.vbox.addLayout(self.hbox0)
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)
        self.vbox.addLayout(self.hbox6)
        self.vbox.addLayout(self.hbox7)

        self.setLayout(self.vbox)

        self.show()
        self.action = Action()


    def button_clicked(self):
        key = self.sender().text()

        if key == '입력':
            # 배부름 게이지바 업데이트
            self.hunger_text.setText(self.action.feeding(self.feed_edit.text()))
            self.feed_edit.clear()
            self.clean_text.setText(self.action.washing(-10))
            self.tired_text.setText(self.action.sleeping(-10))
            self.status_text.setText("먹는중~")
            self.all_text.setText(self.action.currentAll)

        elif key == '씻기기':
            # 청결 게이지바 업데이트
            self.clean_text.setText(self.action.washing(100))
            self.hunger_text.setText(self.action.feeding(-10))
            self.tired_text.setText(self.action.sleeping(-10))
            self.status_text.setText("씻는중~")
            self.all_text.setText(self.action.currentAll)

        elif key == '재우기':
            # 피로 게이지바 업데이트
            self.tired_text.setText(self.action.sleeping(50))
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.status_text.setText("자는중~")
            self.all_text.setText(self.action.currentAll)

        elif key == '공부시키기':
            # 스트레스 게이지바 업데이트
            self.stress_text.setText(self.action.studying())
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.tired_text.setText(self.action.sleeping(-10))
            self.status_text.setText("공부중~")
            self.age_output.setText(str(self.age))
            self.all_text.setText(self.action.currentAll)

        elif key == '놀아주기':
            # 스트레스 게이지바 업데이트
            self.stress_text.setText(self.action.playing())
            self.hunger_text.setText(self.action.feeding(-10))
            self.clean_text.setText(self.action.washing(-10))
            self.tired_text.setText(self.action.sleeping(-10))
            self.status_text.setText("노는중~")
            self.all_text.setText(self.action.currentAll)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Tamagotchi()
    sys.exit(app.exec_())