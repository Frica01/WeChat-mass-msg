# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aboutZmLqYf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 300)
        Frame.setStyleSheet(u"*{\n"
"	font: 14px \"Microsoft YaHei\";\n"
"	color:rgb(0, 0, 0);\n"
"}\n"
"/* \u4e3b\u4f53\u989c\u8272\n"
".QWidget#centralwidget{\n"
"	background-color: rgb(156, 156, 156);\n"
"	border-radius:20px;\n"
"} */\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
".QWidget#mainwidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"/* \u7f16\u8f91\u6846\u6837\u5f0f */\n"
"QLineEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"QLineEdit:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 238, 238);\n"
"}\n"
"\n"
"/* \u6309\u94ae\u6837\u5f0f */\n"
"QPushButton[flat=\"false\"]#button_bug,#button_access{\n"
"	background-color: rgb(255, 153, 153);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"	font: 15px \"Microsoft YaHei\";\n"
"}\n"
"QPushButton:hover#button_bug,QPushButton:hover#button_access{\n"
"	backg"
                        "round-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 153, 153, 255), stop:1 rgba(255, 136, 136, 255));\n"
"}\n"
"QPushButton:pressed#button_bug,QPushButton:pressed#button_access{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 115, 115, 255), stop:1 rgba(255, 153, 153, 255));\n"
"}\n"
"QPushButton#button_close{\n"
"	background-color: rgb(255, 102, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#button_close:pressed{\n"
"	background-color: rgb(200, 80, 80);\n"
"}\n"
"QPushButton#button_max{\n"
"	background-color: rgb(255, 255, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#button_max:pressed{\n"
"	background-color: rgb(195, 195, 78);\n"
"}\n"
"QPushButton#button_min{\n"
"	background-color: rgb(153, 204, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#button_min:pressed{\n"
"	background-color: rgb(126, 168, 83);\n"
"}\n"
"\n"
"\n"
"/* \u6587\u672c\u6846\u6837\u5f0f */\n"
"QPlainTextEdit{\n"
"	border-radius: 15px;\n"
"	border: 2"
                        "px solid rgb(255, 153, 153);\n"
"	padding: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.mainwidget = QWidget(Frame)
        self.mainwidget.setObjectName(u"mainwidget")
        self.mainwidget.setGeometry(QRect(20, 10, 361, 271))
        self.button_close = QPushButton(self.mainwidget)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(330, 20, 16, 16))
        self.button_close.setFlat(True)
        self.button_min = QPushButton(self.mainwidget)
        self.button_min.setObjectName(u"button_min")
        self.button_min.setGeometry(QRect(270, 20, 16, 16))
        self.button_min.setFlat(True)
        self.button_max = QPushButton(self.mainwidget)
        self.button_max.setObjectName(u"button_max")
        self.button_max.setGeometry(QRect(300, 20, 16, 16))
        self.button_max.setFlat(True)
        self.label = QLabel(self.mainwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 111, 41))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"*{\n"
"	font: 18px \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"}\n"
"")
        self.button_bug = QPushButton(self.mainwidget)
        self.button_bug.setObjectName(u"button_bug")
        self.button_bug.setGeometry(QRect(40, 230, 91, 31))
        self.button_access = QPushButton(self.mainwidget)
        self.button_access.setObjectName(u"button_access")
        self.button_access.setGeometry(QRect(220, 230, 91, 31))
        self.textBrowser = QTextBrowser(self.mainwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(40, 70, 281, 131))

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.button_close.setText("")
        self.button_min.setText("")
        self.button_max.setText("")
        self.label.setText(QCoreApplication.translate("Frame", u"\u5173\u4e8e\u7a0b\u5e8f", None))
        self.button_bug.setText(QCoreApplication.translate("Frame", u"BUG\u53cd\u9988", None))
        self.button_access.setText(QCoreApplication.translate("Frame", u"\u5f00\u53d1\u8005\u7f51\u7ad9", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Frame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u8f93\u5165 </span><span style=\" font-size:14px; font-weight:600;\">\u6587\u672c</span><span style=\" font-size:14px;\">\u3001</span><span style=\" font-size:14px; font-weight:600;\">\u6587\u4ef6\uff08\u53ef\u9009\uff09</span><span style=\" font-size:14px;\">\u3001</span><span style=\" font-size:14px; font-weight:600;\">\u6536\u4ef6\u4eba</span><span style=\" font-size:14px;\">\u5373\u53ef\u5f00\u59cb\u53d1\u9001\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-bl"
                        "ock-indent:0; text-indent:0px;\"><span style=\" font-size:14px;\">\u5982\u6807\u9898\u6240\u793a\uff0c\u8be5\u5de5\u5177\u53ea\u652f\u6301\u5728Windows\u7cfb\u7edf\u8fd0\u884c\uff0c\u6709\u95ee\u9898\u8bf7\u4e0e\u6211\u8054\u7cfb\u3002\u8bf7\u52ff\u5c06\u8be5\u5de5\u5177\u7528\u5728\u4efb\u4f55\u8fdd\u6cd5\u7684\u5730\u65b9\uff01</span></p></body></html>", None))
    # retranslateUi

