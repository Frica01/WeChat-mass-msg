# -*- coding: utf-8 -*-

import copy

from PySide2.QtCore import (Qt, QPoint)
from PySide2.QtWidgets import (QMainWindow, QFileDialog, QGraphicsDropShadowEffect, QAction)

from gui.ui.main_ui import UiMainWindow
from gui.win.about_win import AboutWindow
from wechat_operation.wx_operation import WxOperation


def wx_operation(data: list):
    # 暂不考虑重名的好友
    friend_list = list()
    wx = WxOperation()
    msgs, newline_msg, files, friends, tags, all_friend = data
    msgs_list = list()
    if msgs:
        msgs_list = [msg for msg in msgs.split('\n')]
    if newline_msg:
        msgs_list.extend(['\n'.join(newline_msg.split('\n'))])

    if all_friend:
        friend_list: list = wx.get_friend_list()
    else:
        if friends:
            for friend in friends.split():
                friend_list.append(friend)
        if tags:
            for tag in tags.split():
                [friend_list.append(_) for _ in wx.get_friend_list(tag=tag)]
    wx.send_msg(*friend_list, msgs=msgs_list, file_paths=files)


class MainWindow(QMainWindow, UiMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 窗口移动、设置鼠标动作位置
        self._move = False
        self.m_position = QPoint(0, 0)
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(30)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)
        # 绑定checkbox
        self.cbox_select_tag.clicked.connect(self.set_tag_checkbox)
        #
        self.button_close.clicked.connect(lambda: self.close())
        self.button_min.clicked.connect(lambda: self.showMinimized())
        #
        self.button_about.clicked.connect(lambda: AboutWindow().show())
        self.button_send.clicked.connect(self.get_panel_data)
        self.button_reset_msg.clicked.connect(self.te_msg.clear)
        self.button_reset_addressee.clicked.connect(self.reset_addressee)
        self.button_reset_file.clicked.connect(self.lw_select_file.clear)
        self.button_reset_all.clicked.connect(self.reset_all)
        self.button_select_file.clicked.connect(self.select_files)
        # 存放文件的集合
        self.file_set = set()
        # 可拖拽文件
        self.drag_and_drop_files = list()
        self.setAcceptDrops(True)
        # 处理 文件（删除 和 右键菜单
        self.init_context_menu()
        #

    def get_panel_data(self):
        msgs = self.te_msg.toPlainText()
        newline_msg = self.te_msg_newline.toPlainText()
        files = [self.lw_select_file.item(row).text() for row in range(self.lw_select_file.count())]
        friends = self.te_input_f_name.toPlainText()
        tags = self.te_tag.toPlainText()
        all_friend = True if self.cbox_select_all_f.checkState() else False
        wx_operation(data=[msgs, newline_msg, files, friends, tags, all_friend])

    def reset_addressee(self):
        self.te_input_f_name.clear()
        self.te_tag.clear()
        self.cbox_select_tag.setChecked(False)
        self.cbox_select_all_f.setChecked(False)
        self.te_tag.setReadOnly(True)

    def reset_all(self):
        self.te_input_f_name.clear()
        self.te_tag.clear()
        self.cbox_select_tag.setChecked(False)
        self.te_tag.setReadOnly(True)
        self.cbox_select_all_f.setChecked(False)
        self.te_msg.clear()
        self.te_input_f_name.clear()
        self.te_tag.clear()
        self.lw_select_file.clear()

    def select_files(self):
        """选择文件"""
        # 处理删除文件
        self.file_set = set()
        [self.file_set.add(self.lw_select_file.item(row).text()) for row in range(self.lw_select_file.count())]
        old_file_set = copy.deepcopy(self.file_set)
        # 处理拖拽文件
        if self.drag_and_drop_files:
            [self.file_set.add(_.toLocalFile()) for _ in self.drag_and_drop_files]
            self.drag_and_drop_files = list()
        # 处理点击 选择文件
        else:
            file_paths = QFileDialog.getOpenFileNames(self, '选择文件', '*')[0]
            # 如果文件路径存在，就添加到 self.file_set
            if file_paths:
                [self.file_set.add(_) for _ in file_paths]
        # 插入新增的数据
        if self.file_set.difference(old_file_set):
            self.lw_select_file.addItems(self.file_set.difference(old_file_set))

    def init_context_menu(self):
        # 允许右键菜单
        self.lw_select_file.setContextMenuPolicy(Qt.ActionsContextMenu)
        # # 具体菜单项
        right_menu = QAction(self.lw_select_file)
        right_menu.setText('删除')
        # 绑定事件
        right_menu.triggered.connect(
            lambda: self.lw_select_file.takeItem(self.lw_select_file.row(self.lw_select_file.currentItem())))
        # 添加具体的右键菜单
        self.lw_select_file.addAction(right_menu)

    def set_tag_checkbox(self):
        """设置输入标签"""
        if self.cbox_select_tag.checkState():
            self.te_tag.setReadOnly(False)
        else:
            self.te_tag.setReadOnly(True)
            self.te_tag.clear()

    # 拖动进入事件(文件拖拽)
    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            self.drag_and_drop_files = event.mimeData().urls()
            event.accept()  # 鼠标放开函数事件
            self.select_files()
        else:
            event.ignore()

    # 鼠标点击事件产生
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._move = True
            self.m_position = event.globalPos() - self.pos()
            event.accept()

    # 鼠标移动事件
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self._move:
            self.move(QMouseEvent.globalPos() - self.m_position)
            QMouseEvent.accept()

    # 鼠标释放事件
    def mouseReleaseEvent(self, QMouseEvent):
        self._move = False
