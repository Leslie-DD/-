# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changesecret.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changSecretForm(object):
    def setupUi(self, changSecretForm):
        changSecretForm.setObjectName("changSecretForm")
        changSecretForm.resize(449, 277)
        changSecretForm.setMinimumSize(QtCore.QSize(449, 277))
        changSecretForm.setMaximumSize(QtCore.QSize(449, 277))
        self.oldSeretEdit = QtWidgets.QLineEdit(changSecretForm)
        self.oldSeretEdit.setGeometry(QtCore.QRect(170, 28, 200, 30))
        self.oldSeretEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.oldSeretEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.oldSeretEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.oldSeretEdit.setClearButtonEnabled(True)
        self.oldSeretEdit.setObjectName("oldSeretEdit")
        self.newSecretEdit = QtWidgets.QLineEdit(changSecretForm)
        self.newSecretEdit.setGeometry(QtCore.QRect(170, 85, 200, 30))
        self.newSecretEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.newSecretEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.newSecretEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.newSecretEdit.setClearButtonEnabled(True)
        self.newSecretEdit.setObjectName("newSecretEdit")
        self.repeatSecretEdit = QtWidgets.QLineEdit(changSecretForm)
        self.repeatSecretEdit.setGeometry(QtCore.QRect(170, 142, 200, 30))
        self.repeatSecretEdit.setMinimumSize(QtCore.QSize(200, 30))
        self.repeatSecretEdit.setMaximumSize(QtCore.QSize(200, 30))
        self.repeatSecretEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatSecretEdit.setClearButtonEnabled(True)
        self.repeatSecretEdit.setObjectName("repeatSecretEdit")
        self.label = QtWidgets.QLabel(changSecretForm)
        self.label.setGeometry(QtCore.QRect(30, 28, 130, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(changSecretForm)
        self.label_2.setGeometry(QtCore.QRect(30, 85, 130, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(changSecretForm)
        self.label_3.setGeometry(QtCore.QRect(30, 142, 130, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.confirmButton = QtWidgets.QPushButton(changSecretForm)
        self.confirmButton.setGeometry(QtCore.QRect(240, 220, 61, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.confirmButton.setFont(font)
        self.confirmButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirmButton.setStyleSheet("border-image: url(:/button/button.png);")
        self.confirmButton.setObjectName("confirmButton")
        self.cancelButton = QtWidgets.QPushButton(changSecretForm)
        self.cancelButton.setGeometry(QtCore.QRect(140, 220, 61, 30))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.cancelButton.setFont(font)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet("border-image: url(:/button/button.png);")
        self.cancelButton.setObjectName("cancelButton")
        self.label_4 = QtWidgets.QLabel(changSecretForm)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 451, 281))
        self.label_4.setStyleSheet("image: url(:/login/login_400_250.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.oldSeretEdit.raise_()
        self.newSecretEdit.raise_()
        self.repeatSecretEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.confirmButton.raise_()
        self.cancelButton.raise_()

        self.retranslateUi(changSecretForm)
        self.cancelButton.clicked.connect(changSecretForm.cancelChange)
        self.confirmButton.clicked.connect(changSecretForm.confirmChange)
        QtCore.QMetaObject.connectSlotsByName(changSecretForm)

    def retranslateUi(self, changSecretForm):
        _translate = QtCore.QCoreApplication.translate
        changSecretForm.setWindowTitle(_translate("changSecretForm", "密码修改"))
        self.label.setText(_translate("changSecretForm", "原始密码"))
        self.label_2.setText(_translate("changSecretForm", "新密码"))
        self.label_3.setText(_translate("changSecretForm", " 确认新密码"))
        self.confirmButton.setText(_translate("changSecretForm", "修改"))
        self.cancelButton.setText(_translate("changSecretForm", "取消"))
import back_rc
