# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tip.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tipForm(object):
    def setupUi(self, tipForm):
        tipForm.setObjectName("tipForm")
        tipForm.resize(450, 150)
        tipForm.setMinimumSize(QtCore.QSize(450, 150))
        tipForm.setMaximumSize(QtCore.QSize(450, 150))
        font = QtGui.QFont()
        font.setKerning(False)
        tipForm.setFont(font)
        tipForm.setAcceptDrops(False)
        self.contentLabel = QtWidgets.QLabel(tipForm)
        self.contentLabel.setGeometry(QtCore.QRect(25, 0, 400, 100))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setKerning(False)
        self.contentLabel.setFont(font)
        self.contentLabel.setTextFormat(QtCore.Qt.PlainText)
        self.contentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.contentLabel.setObjectName("contentLabel")
        self.pushButton = QtWidgets.QPushButton(tipForm)
        self.pushButton.setGeometry(QtCore.QRect(160, 90, 131, 51))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-image: url(:/button/button.png);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(tipForm)
        self.label.setGeometry(QtCore.QRect(0, 0, 450, 150))
        self.label.setStyleSheet("image: url(:/tip/tip.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.raise_()
        self.contentLabel.raise_()
        self.pushButton.raise_()

        self.retranslateUi(tipForm)
        self.pushButton.clicked.connect(tipForm.closeWindow)
        QtCore.QMetaObject.connectSlotsByName(tipForm)

    def retranslateUi(self, tipForm):
        _translate = QtCore.QCoreApplication.translate
        tipForm.setWindowTitle(_translate("tipForm", "提示"))
        self.contentLabel.setText(_translate("tipForm", "注 册 成 功"))
        self.pushButton.setText(_translate("tipForm", "OK"))
import back_rc
