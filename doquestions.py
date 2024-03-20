from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
import sys
from choose import Ui_chooseForm

class Choice(QWidget, Ui_chooseForm):
    def __init__(self):
        super(Choice, self).__init__()
        self.setupUi(self)

        #self.backButton.clicked.connect(chooseForm.backToLogin)
        #self.startButton.clicked.connect(chooseForm.startDoing)
        #self.changeSecretButton.clicked.connect(chooseForm.changeSecret)
    def backToLogin(self):
        self.close()
        print("返回登陆界面")
    def startDoing(self):
        if self.primaryButton.isChecked() == True and self.quesNumberBox.text()!=0:
            print("小学题目")
        elif self.middleButton.isChecked() == True and self.quesNumberBox.text()!=0:
            print("初中题目")
        elif self.highButton.isChecked() == True and self.quesNumberBox.text()!=0:
            print("高中题目")
        else :
            print("请设置题目数量和题目难度")

    def changeSecret(self):
        self.close()
        print("改密码了")

def main():
    app = QApplication(sys.argv)
    win = Choice()
    win.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()