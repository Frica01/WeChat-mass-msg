# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '微信群发工具tQJoKC.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)
# from views.ui import utils_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(455, 632)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(800, 1200))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 454, 632))
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u".QWidget#widget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:20px;\n"
"}\n"
"/* \u8bbe\u7f6e\u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272\u4e3a\u6de1\u84dd\u8272 */\n"
"QPushButton:hover {\n"
"    background-color: #87CEEB; /* \u6de1\u84dd\u8272 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u6309\u94ae\u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272\u4e3a\u6de1\u7eff\u8272 */\n"
"QPushButton:pressed {\n"
"    background-color: #98FB98; /* \u6de1\u7eff\u8272 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u6309\u94ae\u70b9\u51fb\u7ed3\u675f\u540e\u7684\u80cc\u666f\u989c\u8272\u4e3a\u6de1\u7d2b\u8272 */\n"
"QPushButton:checked {\n"
"    background-color: #E6E6FA; /* \u6de1\u7d2b\u8272 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u6309\u94ae\u4e0a\u7684\u5b57\u4f53\u5bb6\u65cf\u548c\u5b57\u4f53\u5927\u5c0f */\n"
"QPushButton {\n"
"	font: 13pt \"Microsoft YaHei UI\";\n"
"	font: bold\n"
"}\n"
"\n"
"\n"
"\n"
"/* \u4e3a\u540d\u4e3a btn_about \u7684 QPushButton \u8bbe\u7f6e\u4e0d\u540c\u6837\u5f0f */\n"
"\n"
"QPushButton["
                        "flat=\"false\"]#btn_about{\n"
"	background-color: rgb(255, 153, 153);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"	font: 12px \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton#btn_about:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 153, 153, 255), stop:1 rgba(255, 136, 136, 255));\n"
"}\n"
"QPushButton#btn_about:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 115, 115, 255), stop:1 rgba(255, 153, 153, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"*{\n"
"	font: 11pt \"Microsoft YaHei\";\n"
"	color:rgb(0, 0, 0);\n"
"}")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_header = QFrame(self.widget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(450, 50))
        self.frame_header.setMaximumSize(QSize(450, 80))
        self.frame_header.setStyleSheet(u"border-color: rgb(0, 255, 255);")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_header_left = QFrame(self.frame_header)
        self.frame_header_left.setObjectName(u"frame_header_left")
        self.frame_header_left.setFrameShape(QFrame.StyledPanel)
        self.frame_header_left.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_header_left)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.frame_header_left)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        font.setBold(False)
        font.setItalic(False)
        self.title.setFont(font)
        self.title.setStyleSheet(u"QLabel#title{\n"
"	font: 25px;\n"
"	font-weight: bord\n"
"}")

        self.gridLayout_4.addWidget(self.title, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_header_left)

        self.frame_header_right = QFrame(self.frame_header)
        self.frame_header_right.setObjectName(u"frame_header_right")
        self.frame_header_right.setStyleSheet(u"/* \u4e3a\u540d\u4e3a btn_about \u7684 QPushButton \u8bbe\u7f6e\u4e0d\u540c\u6837\u5f0f */\n"
"\n"
"QPushButton[flat=\"false\"]#btn_about{\n"
"	background-color: rgb(255, 153, 153);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"	font: 12px \"Microsoft YaHei\";\n"
"}\n"
"\n"
"QPushButton#btn_about:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 153, 153, 255), stop:1 rgba(255, 136, 136, 255));\n"
"}\n"
"QPushButton#btn_about:pressed{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(190, 115, 115, 255), stop:1 rgba(255, 153, 153, 255));\n"
"}\n"
"\n"
"QPushButton#btn_close{\n"
"	background-color: rgb(255, 102, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#btn_close:pressed{\n"
"	background-color: rgb(200, 80, 80);\n"
"}\n"
"QPushButton#btn_max{\n"
"	background-color: rgb(255, 255, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#btn_max:pressed{\n"
"	background-color: rgb(195, 195, 78);\n"
"}\n"
"QPus"
                        "hButton#btn_min{\n"
"	background-color: rgb(153, 204, 102);\n"
"	border-radius:8px;\n"
"}\n"
"QPushButton#btn_min:pressed{\n"
"	background-color: rgb(126, 168, 83);\n"
"}\n"
"")
        self.frame_header_right.setFrameShape(QFrame.StyledPanel)
        self.frame_header_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_header_right)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_header_right_top = QFrame(self.frame_header_right)
        self.frame_header_right_top.setObjectName(u"frame_header_right_top")
        self.frame_header_right_top.setFrameShape(QFrame.StyledPanel)
        self.frame_header_right_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_header_right_top)
        self.horizontalLayout_6.setSpacing(8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_min = QPushButton(self.frame_header_right_top)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMaximumSize(QSize(16, 16))
        self.btn_min.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_min, 0, Qt.AlignRight)

        self.btn_max = QPushButton(self.frame_header_right_top)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(16, 16))
        self.btn_max.setMaximumSize(QSize(16, 16))
        self.btn_max.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.frame_header_right_top)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setFlat(True)

        self.horizontalLayout_6.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame_header_right_top, 0, Qt.AlignRight)

        self.frame_header_right_bottom = QFrame(self.frame_header_right)
        self.frame_header_right_bottom.setObjectName(u"frame_header_right_bottom")
        self.frame_header_right_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_header_right_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_header_right_bottom)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_about = QPushButton(self.frame_header_right_bottom)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(30, 20))
        self.btn_about.setMaximumSize(QSize(30, 20))

        self.verticalLayout_5.addWidget(self.btn_about, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.frame_header_right_bottom)


        self.horizontalLayout_5.addWidget(self.frame_header_right)


        self.gridLayout_3.addWidget(self.frame_header, 0, 0, 1, 1)

        self.frame_button = QFrame(self.widget)
        self.frame_button.setObjectName(u"frame_button")
        self.frame_button.setMinimumSize(QSize(0, 50))
        self.frame_button.setMaximumSize(QSize(16777215, 50))
        self.frame_button.setStyleSheet(u"")
        self.frame_button.setFrameShape(QFrame.StyledPanel)
        self.frame_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_button)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_reset_all = QPushButton(self.frame_button)
        self.btn_reset_all.setObjectName(u"btn_reset_all")
        self.btn_reset_all.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_reset_all)

        self.btn_send = QPushButton(self.frame_button)
        self.btn_send.setObjectName(u"btn_send")
        self.btn_send.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_send)

        self.btn_pause_or_continue = QPushButton(self.frame_button)
        self.btn_pause_or_continue.setObjectName(u"btn_pause_or_continue")
        self.btn_pause_or_continue.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btn_pause_or_continue)


        self.gridLayout_3.addWidget(self.frame_button, 5, 0, 1, 1)

        self.group_box_msg = QGroupBox(self.widget)
        self.group_box_msg.setObjectName(u"group_box_msg")
        self.group_box_msg.setMinimumSize(QSize(450, 150))
        self.group_box_msg.setMaximumSize(QSize(450, 150))
        self.group_box_msg.setStyleSheet(u"\n"
"QGroupBox {\n"
"	border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(0, 0, 255, 255), stop:1 rgba(0, 255, 0, 255));\n"
"}\n"
"\n"
"QFrame#frame_msg_right{\n"
"	    border: 1px solid ;\n"
"}\n"
"")
        self.group_box_msg.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.horizontalLayout_3 = QHBoxLayout(self.group_box_msg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 15, 5, 5)
        self.frame_msg_left = QFrame(self.group_box_msg)
        self.frame_msg_left.setObjectName(u"frame_msg_left")
        self.frame_msg_left.setMinimumSize(QSize(0, 80))
        self.frame_msg_left.setFrameShape(QFrame.StyledPanel)
        self.frame_msg_left.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_msg_left)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.text_edit_msg = QTextEdit(self.frame_msg_left)
        self.text_edit_msg.setObjectName(u"text_edit_msg")
        self.text_edit_msg.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.text_edit_msg, 0, 0, 1, 1)

        self.text_edit_msg_newline = QTextEdit(self.frame_msg_left)
        self.text_edit_msg_newline.setObjectName(u"text_edit_msg_newline")
        self.text_edit_msg_newline.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.text_edit_msg_newline, 0, 1, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_msg_left)

        self.frame_msg_right = QFrame(self.group_box_msg)
        self.frame_msg_right.setObjectName(u"frame_msg_right")
        self.frame_msg_right.setMinimumSize(QSize(126, 0))
        self.frame_msg_right.setMaximumSize(QSize(126, 16777215))
        self.frame_msg_right.setFrameShape(QFrame.StyledPanel)
        self.frame_msg_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_msg_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cbox_add_remark_name = QCheckBox(self.frame_msg_right)
        self.cbox_add_remark_name.setObjectName(u"cbox_add_remark_name")

        self.verticalLayout_2.addWidget(self.cbox_add_remark_name)

        self.btn_reset_msg_input = QPushButton(self.frame_msg_right)
        self.btn_reset_msg_input.setObjectName(u"btn_reset_msg_input")
        self.btn_reset_msg_input.setMinimumSize(QSize(0, 30))

        self.verticalLayout_2.addWidget(self.btn_reset_msg_input)


        self.horizontalLayout_3.addWidget(self.frame_msg_right)


        self.gridLayout_3.addWidget(self.group_box_msg, 1, 0, 1, 1)

        self.group_box_recipient = QGroupBox(self.widget)
        self.group_box_recipient.setObjectName(u"group_box_recipient")
        self.group_box_recipient.setMinimumSize(QSize(450, 150))
        self.group_box_recipient.setMaximumSize(QSize(450, 150))
        self.group_box_recipient.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(128, 0, 128, 255), stop:1 rgba(255, 20, 147, 255));\n"
"	border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */\n"
"}\n"
"\n"
"QFrame#frame_recipient_right{\n"
"	    border: 1px solid ;\n"
"}")
        self.group_box_recipient.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.horizontalLayout_4 = QHBoxLayout(self.group_box_recipient)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 15, 5, 5)
        self.frame_recipient_left = QFrame(self.group_box_recipient)
        self.frame_recipient_left.setObjectName(u"frame_recipient_left")
        self.frame_recipient_left.setFrameShape(QFrame.StyledPanel)
        self.frame_recipient_left.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_recipient_left)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.text_edit_recipient = QTextEdit(self.frame_recipient_left)
        self.text_edit_recipient.setObjectName(u"text_edit_recipient")

        self.gridLayout_5.addWidget(self.text_edit_recipient, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_recipient_left)

        self.frame_recipient_right = QFrame(self.group_box_recipient)
        self.frame_recipient_right.setObjectName(u"frame_recipient_right")
        self.frame_recipient_right.setMinimumSize(QSize(126, 0))
        self.frame_recipient_right.setMaximumSize(QSize(12, 16777215))
        self.frame_recipient_right.setFrameShape(QFrame.StyledPanel)
        self.frame_recipient_right.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_recipient_right)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.btn_reset_recipient = QPushButton(self.frame_recipient_right)
        self.btn_reset_recipient.setObjectName(u"btn_reset_recipient")
        self.btn_reset_recipient.setMinimumSize(QSize(0, 30))

        self.gridLayout_2.addWidget(self.btn_reset_recipient, 2, 0, 1, 1)

        self.radio_btn_specify_tag = QRadioButton(self.frame_recipient_right)
        self.radio_btn_specify_tag.setObjectName(u"radio_btn_specify_tag")

        self.gridLayout_2.addWidget(self.radio_btn_specify_tag, 0, 0, 1, 1)

        self.radio_btn_specify_group = QRadioButton(self.frame_recipient_right)
        self.radio_btn_specify_group.setObjectName(u"radio_btn_specify_group")

        self.gridLayout_2.addWidget(self.radio_btn_specify_group, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_recipient_right)


        self.gridLayout_3.addWidget(self.group_box_recipient, 3, 0, 1, 1)

        self.group_box_file = QGroupBox(self.widget)
        self.group_box_file.setObjectName(u"group_box_file")
        self.group_box_file.setMinimumSize(QSize(450, 150))
        self.group_box_file.setMaximumSize(QSize(450, 150))
        self.group_box_file.setStyleSheet(u"QGroupBox {\n"
"    border: 2px solid qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 165, 0, 255));\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QFrame#frame_file_right{\n"
"	    border: 1px solid ;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QListWidget {\n"
"	background-color: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */\n"
"	border: transparent; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272\u4e3a\u900f\u660e */\n"
"}")
        self.group_box_file.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.horizontalLayout_2 = QHBoxLayout(self.group_box_file)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 15, 5, 5)
        self.frame_file_left = QFrame(self.group_box_file)
        self.frame_file_left.setObjectName(u"frame_file_left")
        self.frame_file_left.setFrameShape(QFrame.StyledPanel)
        self.frame_file_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_file_left)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.list_widget_file = QListWidget(self.frame_file_left)
        self.list_widget_file.setObjectName(u"list_widget_file")
        self.list_widget_file.setMaximumSize(QSize(300, 16777215))

        self.verticalLayout_4.addWidget(self.list_widget_file)


        self.horizontalLayout_2.addWidget(self.frame_file_left)

        self.frame_file_right = QFrame(self.group_box_file)
        self.frame_file_right.setObjectName(u"frame_file_right")
        self.frame_file_right.setMinimumSize(QSize(126, 0))
        self.frame_file_right.setMaximumSize(QSize(126, 16777215))
        self.frame_file_right.setFrameShape(QFrame.StyledPanel)
        self.frame_file_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_file_right)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_add_file = QPushButton(self.frame_file_right)
        self.btn_add_file.setObjectName(u"btn_add_file")
        self.btn_add_file.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.btn_add_file)

        self.btn_reset_file = QPushButton(self.frame_file_right)
        self.btn_reset_file.setObjectName(u"btn_reset_file")
        self.btn_reset_file.setMinimumSize(QSize(0, 30))

        self.verticalLayout_3.addWidget(self.btn_reset_file)


        self.horizontalLayout_2.addWidget(self.frame_file_right)


        self.gridLayout_3.addWidget(self.group_box_file, 2, 0, 1, 1)

        self.frame_progress = QFrame(self.widget)
        self.frame_progress.setObjectName(u"frame_progress")
        self.frame_progress.setStyleSheet(u"QFrame#frame_progress{\n"
"	    border: 1px solid ;	\n"
"		border-radius: 10px; /* \u8bbe\u7f6e\u5706\u89d2\u534a\u5f84 */	\n"
"}")
        self.frame_progress.setFrameShape(QFrame.StyledPanel)
        self.frame_progress.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_progress)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.progress_label = QLabel(self.frame_progress)
        self.progress_label.setObjectName(u"progress_label")

        self.horizontalLayout_7.addWidget(self.progress_label, 0, Qt.AlignHCenter)

        self.progress_bar = QProgressBar(self.frame_progress)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)
        self.progress_bar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.progress_bar, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_3.addWidget(self.frame_progress, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Win\u5fae\u4fe1\u7fa4\u53d1\u5de5\u5177", None))
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_close.setText("")
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.btn_reset_all.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u5168\u90e8", None))
        self.btn_send.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u53d1\u9001", None))
        self.btn_pause_or_continue.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u53d1\u9001", None))
        self.group_box_msg.setTitle(QCoreApplication.translate("MainWindow", u"\u6d88\u606f\u6846", None))
        self.text_edit_msg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u6587\u672c...", None))
        self.text_edit_msg_newline.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5728\u6b64\u5904\u8f93\u5165\u5e26\u6362\u884c\u7684\u6587\u672c...", None))
        self.cbox_add_remark_name.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5907\u6ce8", None))
        self.btn_reset_msg_input.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u8f93\u5165", None))
        self.group_box_recipient.setTitle(QCoreApplication.translate("MainWindow", u"\u6536\u4ef6\u4eba", None))
        self.btn_reset_recipient.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u9009\u62e9", None))
        self.radio_btn_specify_tag.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u597d\u53cb\u6807\u7b7e", None))
        self.radio_btn_specify_group.setText(QCoreApplication.translate("MainWindow", u"\u6307\u5b9a\u7fa4\u804a\u540d\u79f0", None))
        self.group_box_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u6846", None))
        self.btn_add_file.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6587\u4ef6", None))
        self.btn_reset_file.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u9009\u62e9", None))
        self.progress_label.setText(QCoreApplication.translate("MainWindow", u"\u5171xx, \u5df2\u5b8c\u6210xx", None))
    # retranslateUi

