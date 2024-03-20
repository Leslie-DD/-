import sys
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from login import Ui_loginForm
from register import Ui_registerForm
from tip import Ui_tipForm
from choose import Ui_chooseForm
from changesecret import Ui_changSecretForm
from set_questions import Ui_setquestionForm
from score import Ui_scoreForm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QIcon

import readuser
import isregistercorrect
import ischangecorrect
import setquestions
import calculate
import database

'''登陆界面
'''
class Login(QWidget, Ui_loginForm):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./dog.png'))
        #self.gologinButton.clicked.connect(self.loginNow)
        #self.goregisterButton.clicked.connect(self.goRegister)
    '''登录button信号槽
    '''
    def loginNow(self):
        _translate = QtCore.QCoreApplication.translate
        self.isUserExist = 0
        self.isPassCorrect = 0
        # 判断用户名是否存在，密码是否正确
        self.isUserExist, self.isPassCorrect = database.isCorrectOrNot(self.usernameEdit.text(),self.passwordEdit.text())
        #print(self.isUserExist,self.isPassCorrect)
        # 用户名和密码正确
        if self.isUserExist == 1 and self.isPassCorrect ==1:
            username = self.usernameEdit.text()
            self.reg = Choice(username)
            self.reg.show()
            self.close()
        elif self.passwordEdit.text() == "" or self.usernameEdit.text() == ""  :
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.reg.contentLabel.setText(_translate("tipForm", "请输入用户名和密码！"))
            self.reg.show()
        # 用户名存在，密码不正确
        elif self.isUserExist == 1 and self.isPassCorrect ==0:
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.reg.contentLabel.setText(_translate("tipForm", "密码错误！"))
            self.passwordEdit.setText(_translate("loginForm", ""))
            self.reg.show()
        elif self.isUserExist == 0:
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.reg.contentLabel.setText(_translate("tipForm", "用户不存在！"))
            self.reg.show()


        # 用户名不存在

    '''注册button信号槽
    '''
    def goRegister(self):
        #self.close()
        self.reg = Register()
        self.reg.show()

'''注册窗口
'''
class Register(QWidget, Ui_registerForm):
    def __init__(self):
        super(Register, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./dog.png'))
        #self.backButton.clicked.connect(self.backtoLogin)
        #self.registerButton.clicked.connect(self.registerSuccess)
        #self.sendCodeButton.clicked.connect(self.sendCode)
        #self.codeEdit.textChanged['QString'].connect(registerForm.codeChanged)
        #self.numberEdit.textChanged['QString'].connect(registerForm.phoneChanged)
        self.code = ""  # 验证码
        self.isSentcode = 0
        self.usernameEdit.setEnabled(False)
        self.passwordEdit.setEnabled(False)
        self.confirmEdit.setEnabled(False)
    def phoneChanged(self):
        _translate = QtCore.QCoreApplication.translate
        self.sendCodeButton.setEnabled(True)
        self.codeEdit.setEnabled(True)
        self.usernameEdit.setEnabled(False)
        self.passwordEdit.setEnabled(False)
        self.confirmEdit.setEnabled(False)
        self.sendCodeButton.setText(_translate("tipForm", "发送验证码"))
    def codeChanged(self):
        _translate = QtCore.QCoreApplication.translate
        if self.code != "" and self.code == self.codeEdit.text():
            self.sendCodeButton.setText(_translate("tipForm", "输入正确！"))
            self.sendCodeButton.setEnabled(False)
            self.codeEdit.setEnabled(False)
            self.usernameEdit.setEnabled(True)
            self.passwordEdit.setEnabled(True)
            self.confirmEdit.setEnabled(True)
        else :
            self.sendCodeButton.setText(_translate("tipForm", "请输入正确的验证码！"))
            self.sendCodeButton.setEnabled(False)
    '''返回button信号槽，返回登陆界面
    '''
    def backtoLogin(self):
        self.close()
        self.child = Login()
        self.child.show()
    '''发送验证码button信号槽
    '''
    def sendCode(self):
        _translate = QtCore.QCoreApplication.translate
        self.sendCodeButton.setText(_translate("tipForm", "请输入正确的验证码！"))
        self.sendCodeButton.setEnabled(False)
        # 判断是否发送的标志
        self.string, self.number = isregistercorrect.isSendOK(self.numberEdit.text())
        # 电话号码格式正确，符合发送条件，发送
        if self.string == "" and self.number == 1:
            self.code = isregistercorrect.sendCode(self.numberEdit.text())
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "Congratulations!"))
            self.reg.contentLabel.setText(_translate("tipForm", "发送成功！"))
            self.reg.show()
            #self.isSentcode = 1
        # 电话号码格式错误，提示并且不发送
        elif self.string != "" and self.number == 0:
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.reg.contentLabel.setText(_translate("tipForm", self.string))
            self.reg.show()
    '''注册button信号槽
    '''
    def registerSuccess(self):
        _translate = QtCore.QCoreApplication.translate
        # 判断是否满足注册条件的标志
        self.String, self.Number = isregistercorrect.isRegisterCorrect(self.usernameEdit.text(),self.passwordEdit.text(), self.confirmEdit.text(), self.numberEdit.text(), self.codeEdit.text(), self.code)
        # 满足注册条件
        if self.String == "" and self.Number == 1:
            database.insertDb(self.usernameEdit.text(), self.passwordEdit.text())
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "Congratulations!"))
            self.reg.contentLabel.setText(_translate("tipForm", "注册成功！"))
            self.reg.show()
            self.close()
        # 不满足注册条件，提示
        elif self.String != "" and self.Number==0:
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.reg.contentLabel.setText(_translate("tipForm", self.String))
            self.reg.show()
        '''
        elif self.isSentcode == 0:
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.reg.contentLabel.setText(_translate("tipForm", "请发送验证码并输入！"))
            self.reg.show()
        '''
'''选择窗口
'''
class Choice(QWidget, Ui_chooseForm):
    def __init__(self, username, parent = None):
        super(Choice, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./dog.png'))
        #self.backButton.clicked.connect(chooseForm.backToLogin)
        #self.startButton.clicked.connect(chooseForm.startDoing)
        #self.changeSecretButton.clicked.connect(chooseForm.changeSecret)
        self.username = username
    def backToLogin(self):
        self.close()
        self.child = Login()
        self.child.show()
    def startDoing(self):
        _translate = QtCore.QCoreApplication.translate

        if self.quesNumberBox.text() == '0':
            self.child = Tip()
            self.child.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.child.contentLabel.setText(_translate("tipForm", "请选择题目数量！"))
            self.child.show()
        elif  self.quesNumberBox.text()!= '0':
            if int(self.quesNumberBox.text())<10 or int(self.quesNumberBox.text())>30:
                self.child = Tip()
                self.child.setWindowTitle(_translate("tipForm", "WARNING!"))
                self.child.contentLabel.setText(_translate("tipForm", "题目数量：10-30！"))
                self.child.show()
            else:
                questionnumber = self.quesNumberBox.text()
                username = self.username
                if self.primaryButton.isChecked() == True :
                    gradelevel = 0
                    self.child = Question(questionnumber, gradelevel, username)
                    self.child.show()
                    self.close()
                elif self.middleButton.isChecked() == True :
                    gradelevel = 1
                    self.child = Question(questionnumber, gradelevel, username)
                    self.child.show()
                    self.close()
                elif self.highButton.isChecked() == True :
                    gradelevel = 2
                    self.child = Question(questionnumber, gradelevel, username)
                    self.child.show()
                    self.close()
                else:
                    self.child = Tip()
                    self.child.setWindowTitle(_translate("tipForm", "WARNING!"))
                    self.child.contentLabel.setText(_translate("tipForm", "请选择题目难度！"))
                    self.child.show()

    def changeSecret(self):
        username = self.username
        self.child = Secret(username)
        self.child.show()
'''改密码窗口
'''
class Secret(QWidget, Ui_changSecretForm):
    def __init__(self, username):
        super(Secret, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./dog.png'))
        self.username = username
        #print(username)
        #self.cancelButton.clicked.connect(changSecretForm.cancelChange)
        #self.confirmButton.clicked.connect(changSecretForm.confirmChange)
    def cancelChange(self):
        self.close()
    def confirmChange(self):
        _translate = QtCore.QCoreApplication.translate
        self.string, self.prime = ischangecorrect.isChangeCorrect(self.username,self.oldSeretEdit.text(),self.newSecretEdit.text(), self.repeatSecretEdit.text())
        if self.string!="":
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "WARNING!"))
            self.reg.contentLabel.setText(_translate("tipForm", self.string))
            self.reg.show()
        elif self.string == "" and self.prime == 1:
            database.updateDb(self.username, self.oldSeretEdit.text(), self.newSecretEdit.text())
            self.reg = Tip()
            self.reg.setWindowTitle(_translate("tipForm", "Congratulations!"))
            self.reg.contentLabel.setText(_translate("tipForm", "修改成功"))
            self.reg.show()
            self.close()

'''做题窗口
'''
class Question(QMainWindow, Ui_setquestionForm):
    def __init__(self, questionNum, gradelevel, username, parent = None):
        super(Question, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./dog.png'))
        #self.quitLoginButton.clicked.connect(setquestionForm.quitToLogin)
        #self.setQuesButton.clicked.connect(setquestionForm.quitToChoice)
        #self.changeSecretButton.clicked.connect(setquestionForm.changeSecret)
        #self.submitButton.clicked.connect(setquestionForm.submitNow)
        #self.beforeQuesButton.clicked.connect(setquestionForm.beforQues)
        #self.nextQuesButton.clicked.connect(setquestionForm.nextQues)
        #self.ARadio.clicked.connect(setquestionForm.ifisChecked)
        #self.BRadio.clicked.connect(setquestionForm.ifisChecked)
        #self.CRadio.clicked.connect(setquestionForm.ifisChecked)
        #self.DRadio.clicked.connect(setquestionForm.ifisChecked)
        # *********不同窗口间的参数传递*************
        self.username = username
        self.grade = gradelevel
        self.questionNum = questionNum  # 注意这里是字符串类型
        self.quesScore = [0]*int(self.questionNum)
        #print(self.quesScore)

        self.gather = setquestions.set_questions(int(self.questionNum), int(self.grade),  "用户1", str(self.grade) )
        self.answer, self.diction = calculate.all(self.gather)
        #print(self.answer)
        #print(self.diction)
        self.quesCount = 1
        _translate = QtCore.QCoreApplication.translate
        self.quesNoLabel.setText(_translate("setquestionForm", "第 %d 题"%self.quesCount))
        self.quesLabel.setText(_translate("setquestionForm", self.gather[self.quesCount-1]))
        self.ARadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount-1]['A:'])))
        self.BRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount-1]['B:'])))
        self.CRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount-1]['C:'])))
        self.DRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount-1]['D:'])))
        self.beforeQuesButton.setEnabled(False)
        if self.quesCount == int(self.questionNum):
            self.nextQuesButton.setEnabled(False)
    def quitToLogin(self):
        self.close()
        self.child1 = Login()
        self.child1.show()
    def quitToChoice(self):
        self.close()
        self.child2 = Choice(self.username)
        self.child2.show()
    def changeSecret(self):
        self.child3 = Secret(self.username)
        self.child3.show()
    def submitNow(self):
        self.close()
        print("Submit Successfully!")
        self.score = 0
        for i in self.quesScore:
            self.score += i
        print("Score:", self.quesScore, self.score)
        self.score = round((self.score / float(self.questionNum)) * 100, 1)

        _translate = QtCore.QCoreApplication.translate
        username = self.username
        self.child4 = Score(username)
        self.child4.scoreLabel.setText(_translate("scoreForm", str(self.score)))
        self.child4.show()
    def beforQues(self):
        self.quesCount -= 1
        if self.quesCount == 1:
            self.beforeQuesButton.setEnabled(False)
        if self.quesCount != int(self.questionNum):
            self.nextQuesButton.setEnabled(True)
        _translate = QtCore.QCoreApplication.translate
        self.quesNoLabel.setText(_translate("setquestionForm", "第 %d 题" % self.quesCount))
        self.quesLabel.setText(_translate("setquestionForm", self.gather[self.quesCount - 1]))
        self.ARadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['A:'])))
        self.BRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['B:'])))
        self.CRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['C:'])))
        self.DRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['D:'])))

        self.ARadio.setCheckable(False)
        self.ARadio.setCheckable(True)
        self.BRadio.setCheckable(False)
        self.BRadio.setCheckable(True)
        self.CRadio.setCheckable(False)
        self.CRadio.setCheckable(True)
        self.DRadio.setCheckable(False)
        self.DRadio.setCheckable(True)
        print("before")
    def nextQues(self):
        self.quesCount += 1
        print(self.quesCount)
        print(self.questionNum)
        if self.quesCount != 1:
            self.beforeQuesButton.setEnabled(True)
        if self.quesCount == int(self.questionNum):
            self.nextQuesButton.setEnabled(False)
        _translate = QtCore.QCoreApplication.translate
        self.quesNoLabel.setText(_translate("setquestionForm", "第 %d 题" % self.quesCount))
        self.quesLabel.setText(_translate("setquestionForm", self.gather[self.quesCount - 1]))
        self.ARadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['A:'])))
        self.BRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['B:'])))
        self.CRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['C:'])))
        self.DRadio.setText(_translate("setquestionForm", str(self.diction[self.quesCount - 1]['D:'])))

        self.ARadio.setCheckable(False)
        self.ARadio.setCheckable(True)
        self.BRadio.setCheckable(False)
        self.BRadio.setCheckable(True)
        self.CRadio.setCheckable(False)
        self.CRadio.setCheckable(True)
        self.DRadio.setCheckable(False)
        self.DRadio.setCheckable(True)
        print("next")
    def ifisChecked(self):
        if self.ARadio.isChecked() == True and str(self.answer[self.quesCount-1]) == str(self.diction[self.quesCount-1]['A:']):
            self.quesScore[self.quesCount-1] = 1
        elif self.BRadio.isChecked() == True and str(self.answer[self.quesCount - 1]) == str(self.diction[self.quesCount - 1]['B:']):
            self.quesScore[self.quesCount - 1] = 1
        elif self.CRadio.isChecked() == True and str(self.answer[self.quesCount - 1]) == str(self.diction[self.quesCount - 1]['C:']):
            self.quesScore[self.quesCount - 1] = 1
        elif self.DRadio.isChecked() == True and str(self.answer[self.quesCount - 1]) == str(self.diction[self.quesCount - 1]['D:']):
            self.quesScore[self.quesCount - 1] = 1
        elif self.ARadio.isChecked() == False :
            self.quesScore[self.quesCount-1] = 0
        elif self.BRadio.isChecked() == False :
            self.quesScore[self.quesCount - 1] = 0
        elif self.CRadio.isChecked() == False :
            self.quesScore[self.quesCount - 1] = 0
        elif self.DRadio.isChecked() == False :
            self.quesScore[self.quesCount - 1] = 0
'''得分窗口
'''
class Score(QMainWindow, Ui_scoreForm):
    def __init__(self, username):
        super(Score, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./dog.png'))
        self.username = username
        #self.backtologinButton.clicked.connect(scoreForm.backToLogin)
        #self.backtochoiceButton.clicked.connect(scoreForm.backToChoice)
        #self.changeSecretButton.clicked.connect(scoreForm.toChange)

    def backToLogin(self):
        self.close()
        self.child1 = Login()
        self.child1.show()
    def backToChoice(self):
        self.close()
        self.child2 = Choice(self.username)
        self.child2.show()
    def toChange(self):
        self.reg = Secret(self.username)
        self.reg.show()


'''提示框
'''
class Tip(QWidget, Ui_tipForm):
    def __init__(self):
        super(Tip, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./dog.png'))
        #self.pushButton.clicked.connect(tipForm.closeWindow)
    def closeWindow(self):
        self.close()

def main():
    app = QApplication(sys.argv)
    win = Login()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
