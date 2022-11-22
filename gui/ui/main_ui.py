# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledFKRcRg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(522, 600)
        MainWindow.setStyleSheet(u"*{\n"
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
"QLabel#label_title{\n"
"	font: 25px;\n"
"	font-weight: bord\n"
"}\n"
".QWidget#widget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:20px;\n"
"}\n"
"\n"
"/* \u7f16\u8f91\u6846\u6837\u5f0f */\n"
"QTextEdit{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"QTextEdit#te_msg{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"\n"
"QLineEdit:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 238, 238);\n"
"}\n"
"\n"
"/* \u6309\u94ae\u6837\u5f0f"
                        " */\n"
"QPushButton[flat=\"false\"]{\n"
"	background-color: rgb(255, 153, 153);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"	font: 15px \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton[flat=\"false\"]#button_about{\n"
"	background-color: rgb(255, 153, 153);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"	font: 12px \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 153, 153, 255), stop:1 rgba(255, 136, 136, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 115, 115, 255), stop:1 rgba(255, 153, 153, 255));\n"
"}\n"
"\n"
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
"QPus"
                        "hButton#button_max:pressed{\n"
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
"/* \u9009\u62e9\u8868\u6837\u5f0f */\n"
"QListWidget{\n"
"	border: 2px solid rgb(255, 255, 255);\n"
"	border-radius:15px;\n"
"	padding: 5px;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget::item{\n"
"	border: 1px dashed rgb(255, 204, 153);\n"
"	border-radius: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget::item:hover{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 204, 153);\n"
"}\n"
"QListWidget::item:focus{\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"/* \u5206\u7ec4\u6846\u6837\u5f0f */\n"
"QGroupBox{\n"
"	border: 2px solid rgb(255, 153, 153);\n"
"	border-radius: 15px;\n"
"	margin-top: 2ex;\n"
"}\n"
"QGroupBox::title{\n"
"	subcontrol-origin: margin;\n"
"	subcontrol-"
                        "position: top center;\n"
"	padding: 0 3px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 30, 421, 521))
        self.gbox_file = QGroupBox(self.widget)
        self.gbox_file.setObjectName(u"gbox_file")
        self.gbox_file.setGeometry(QRect(10, 200, 401, 121))
        self.button_select_file = QPushButton(self.gbox_file)
        self.button_select_file.setObjectName(u"button_select_file")
        self.button_select_file.setGeometry(QRect(300, 30, 81, 31))
        self.button_reset_file = QPushButton(self.gbox_file)
        self.button_reset_file.setObjectName(u"button_reset_file")
        self.button_reset_file.setGeometry(QRect(300, 80, 81, 31))
        self.gbox_addressee = QGroupBox(self.widget)
        self.gbox_addressee.setObjectName(u"gbox_addressee")
        self.gbox_addressee.setGeometry(QRect(10, 320, 401, 151))
        self.cbox_select_all_f = QCheckBox(self.gbox_addressee)
        self.cbox_select_all_f.setObjectName(u"cbox_select_all_f")
        self.cbox_select_all_f.setGeometry(QRect(290, 30, 101, 31))
        self.cbox_select_tag = QCheckBox(self.gbox_addressee)
        self.cbox_select_tag.setObjectName(u"cbox_select_tag")
        self.cbox_select_tag.setGeometry(QRect(150, 30, 101, 31))
        self.cbox_inpu_f = QCheckBox(self.gbox_addressee)
        self.cbox_inpu_f.setObjectName(u"cbox_inpu_f")
        self.cbox_inpu_f.setGeometry(QRect(20, 30, 101, 31))
        self.cbox_inpu_f.setChecked(True)
        self.cbox_inpu_f.setTristate(False)
        self.te_input_f_name = QTextEdit(self.gbox_addressee)
        self.te_input_f_name.setObjectName(u"te_input_f_name")
        self.te_input_f_name.setGeometry(QRect(10, 60, 121, 81))
        self.button_reset_file_2 = QPushButton(self.gbox_addressee)
        self.button_reset_file_2.setObjectName(u"button_reset_file_2")
        self.button_reset_file_2.setGeometry(QRect(300, 100, 81, 31))
        self.te_tag = QTextEdit(self.gbox_addressee)
        self.te_tag.setObjectName(u"te_tag")
        self.te_tag.setGeometry(QRect(150, 60, 111, 81))
        self.gbox_msg = QGroupBox(self.widget)
        self.gbox_msg.setObjectName(u"gbox_msg")
        self.gbox_msg.setGeometry(QRect(10, 60, 401, 141))
        self.te_msg = QTextEdit(self.gbox_msg)
        self.te_msg.setObjectName(u"te_msg")
        self.te_msg.setGeometry(QRect(10, 20, 381, 111))
        self.lw_select_file = QListWidget(self.widget)
        self.lw_select_file.setObjectName(u"lw_select_file")
        self.lw_select_file.setGeometry(QRect(20, 220, 281, 91))
        self.button_max = QPushButton(self.widget)
        self.button_max.setObjectName(u"button_max")
        self.button_max.setGeometry(QRect(370, 10, 16, 16))
        self.button_max.setFlat(True)
        self.button_close = QPushButton(self.widget)
        self.button_close.setObjectName(u"button_close")
        self.button_close.setGeometry(QRect(400, 10, 16, 16))
        self.button_close.setFlat(True)
        self.button_min = QPushButton(self.widget)
        self.button_min.setObjectName(u"button_min")
        self.button_min.setGeometry(QRect(340, 10, 16, 16))
        self.button_min.setFlat(True)
        self.button_send = QPushButton(self.widget)
        self.button_send.setObjectName(u"button_send")
        self.button_send.setGeometry(QRect(290, 480, 81, 31))
        self.button_reset_all = QPushButton(self.widget)
        self.button_reset_all.setObjectName(u"button_reset_all")
        self.button_reset_all.setGeometry(QRect(50, 480, 81, 31))
        self.label_title = QLabel(self.widget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 10, 211, 31))
        self.button_about = QPushButton(self.widget)
        self.button_about.setObjectName(u"button_about")
        self.button_about.setGeometry(QRect(380, 40, 31, 21))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.gbox_file.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.button_select_file.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.button_reset_file.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u8f93\u5165", None))
        self.gbox_addressee.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6536\u4ef6\u4eba", None))
        self.cbox_select_all_f.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5168\u90e8\u597d\u53cb", None))
        self.cbox_select_tag.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u597d\u53cb\u6807\u7b7e", None))
        self.cbox_inpu_f.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u597d\u53cb\u6635\u79f0", None))
        self.te_input_f_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u597d\u53cb\u6635\u79f0\u4ee5\u6362\u884c\u5206\u5272...", None))
        self.button_reset_file_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u8f93\u5165", None))
        self.te_tag.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u6536\u4ef6\u4eba\u6807\u7b7e\uff0c\u53ef\u4e0d\u9009...", None))
        self.gbox_msg.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u6846", None))
        self.te_msg.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei'; font-size:14px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.te_msg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u6587\u672c...", None))
        self.button_max.setText("")
        self.button_close.setText("")
        self.button_min.setText("")
        self.button_send.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u53d1\u9001", None))
        self.button_reset_all.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u5168\u90e8", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Win\u5fae\u4fe1\u7fa4\u53d1\u5de5\u5177", None))
        self.button_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

