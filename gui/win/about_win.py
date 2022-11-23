# -*- coding: utf-8 -*-

import webbrowser
from PySide2.QtCore import Qt, QPoint
from PySide2.QtWidgets import QWidget, QGraphicsDropShadowEffect

from gui.ui.about_ui import AboutFrame


class AboutWindow(QWidget, AboutFrame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置窗口透明
        self.setWindowModality(Qt.ApplicationModal)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 设置鼠标动作位置
        self.m_Position = QPoint(0, 0)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(30)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        #
        self.button_min.clicked.connect(lambda: self.showMinimized())
        self.button_close.clicked.connect(lambda: self.close())
        #
        self.button_access.clicked.connect(lambda: webbrowser.open('https://space.bilibili.com/39880798'))
        self.button_bug.clicked.connect(lambda: webbrowser.open('https://github.com/Frica01/Wechat_mass_msg/issues'))

    # 鼠标点击事件产生
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.Move = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    # 鼠标移动事件
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.Move:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    # 鼠标释放事件
    def mouseReleaseEvent(self, QMouseEvent):
        self.Move = False
