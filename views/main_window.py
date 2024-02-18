# -*- coding: utf-8 -*-
# Name:         main_window.py
# Author:       小菜
# Date:         2023/11/28 10:35
# Description:

import os

from PySide6.QtCore import (QPoint, Qt)
from PySide6.QtGui import (QAction, QIcon, QShortcut, QKeySequence)
from PySide6.QtWidgets import (QMainWindow, QGraphicsDropShadowEffect, QFileDialog, QMessageBox, QSystemTrayIcon, QMenu)

from views.about_window import AboutWindow
from views.ui.main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        # 首先声明所有实例变量
        self._move = False
        self.m_position = None
        self.drag_and_drop_files = None

        # 使用由Qt Designer生成的Ui类初始化UI
        self.setupUi(self)
        self.init_ui()
        self.init_connections()
        self.init_context_menu()  # 处理 文件（删除 和 右键菜单
        self.init_text_edit_style()
        self.init_drag_and_drop()
        self.init_window_position()
        self.init_progress()

        # 置顶窗口
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        #
        self.listen_keyboard_chain()
        self.flag = True

    def init_ui(self):
        # 隐藏边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.set_graphics_effect()

    @property
    def is_wx_activated(self) -> bool:
        """判断微信是否启动"""
        if not self.controller.has_wx_instance():
            self.show_message_box('严重错误🆘', "微信未启动!", level='error')
            return False
        return True

    def set_graphics_effect(self):
        # 添加阴影
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(30)
        effect.setOffset(0, 0)
        effect.setColor(Qt.gray)
        self.setGraphicsEffect(effect)

    def init_connections(self):
        self.btn_reset_msg_input.clicked.connect(self.text_edit_msg.clear)
        self.btn_reset_msg_input.clicked.connect(self.text_edit_msg_newline.clear)
        self.btn_add_file.clicked.connect(self.select_files)
        self.btn_reset_file.clicked.connect(self.list_widget_file.clear)
        self.btn_reset_recipient.clicked.connect(self.text_edit_recipient.clear)
        self.btn_reset_recipient.clicked.connect(self.reset_radio_btn)
        self.btn_reset_all.clicked.connect(self.reset_all)
        self.btn_send.clicked.connect(self.on_send_clicked)
        self.btn_pause_or_continue.clicked.connect(self.toggle_pause)
        #
        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_min.clicked.connect(lambda: self.showMinimized())
        #
        self.controller.progress_updated.connect(self.update_progress)
        self.btn_about.clicked.connect(lambda: AboutWindow().show())
        #

    def init_text_edit_style(self):
        self.text_edit_msg.setPlaceholderText('在此处输入消息,\n一行为一条内容...')
        self.text_edit_msg_newline.setPlaceholderText('在此处输入消息,\n一共为一条内容...')
        self.text_edit_recipient.setPlaceholderText(
            '默认为 输入好友昵称, 以换行符分隔...\n若勾选 指定好友标签, 则输入标签名称...\n若勾选 选择全部好友, 则无需输入内容...'
        )

    def init_drag_and_drop(self):
        self.drag_and_drop_files = list()
        # 可拖拽
        self.setAcceptDrops(True)

    def init_window_position(self):
        self._move = False
        self.m_position = QPoint(0, 0)

    def init_context_menu(self):
        # 允许右键菜单
        self.list_widget_file.setContextMenuPolicy(Qt.ActionsContextMenu)
        # # 具体菜单项
        right_menu = QAction(self.list_widget_file)
        right_menu.setText('删除')
        # 绑定事件
        right_menu.triggered.connect(
            lambda: self.list_widget_file.takeItem(self.list_widget_file.row(self.list_widget_file.currentItem()))
        )
        # 添加具体的右键菜单
        self.list_widget_file.addAction(right_menu)

    def init_progress(self):
        # 清空下面
        self.progress_label.setText('当前未有任务运行!')
        self.progress_bar.setValue(100)

    def toggle_pause(self):
        self.controller.toggle_pause()
        # 切换按钮文本
        current_text = self.btn_pause_or_continue.text()
        self.btn_pause_or_continue.setText('暂停发送' if current_text == '继续发送' else '继续发送')

    def on_send_clicked(self):
        msgs = self.text_edit_msg.toPlainText()
        newline_msg = self.text_edit_msg_newline.toPlainText()
        add_remark_name = True if self.cbox_add_remark_name.checkState().value else False
        files = [self.list_widget_file.item(row).text() for row in range(self.list_widget_file.count())]
        friends = self.text_edit_recipient.toPlainText()
        is_specify_tag = True if self.radio_btn_specify_tag.isChecked() else False
        is_specify_group = True if self.radio_btn_specify_group.isChecked() else False
        #
        if not any([msgs, files]) or not friends:
            self.show_message_box('警告⚠', "消息和文件不可同时为空\n       联系人不可为空")
            return
        data = {
            'msgs': msgs,
            'newline_msg': newline_msg,
            'add_remark_name': add_remark_name,
            'files': files,
            'friends': friends,
            'is_specify_tag': is_specify_tag,
            'is_specify_group': is_specify_group
        }
        self.controller.start_sending_messages(**data)

    def update_progress(self, current, total):
        if total > 0:
            progress = int((current / total) * 100)
            self.progress_bar.setValue(progress)
            self.progress_label.setText(f"已发送 {current}位好友，需发送 {total}位好友")
        else:
            self.progress_bar.setValue(0)
            self.progress_label.setText("未开始")

    def reset_radio_btn(self):
        self.radio_btn_specify_tag.setAutoExclusive(False)
        self.radio_btn_specify_tag.setChecked(False)
        self.radio_btn_specify_tag.setAutoExclusive(True)
        self.radio_btn_specify_group.setAutoExclusive(False)
        self.radio_btn_specify_group.setChecked(False)
        self.radio_btn_specify_group.setAutoExclusive(True)

    def reset_all(self):
        self.text_edit_msg.clear()
        self.text_edit_msg_newline.clear()
        self.cbox_add_remark_name.setChecked(False)
        #
        self.list_widget_file.clear()
        #
        self.text_edit_recipient.clear()
        #
        self.reset_radio_btn()

    def select_files(self):
        """选择文件并更新列表控件。"""
        # 获取当前列表中的文件
        current_files = {self.list_widget_file.item(row).text() for row in range(self.list_widget_file.count())}

        # 处理拖拽文件
        if self.drag_and_drop_files:
            new_files = {file.toLocalFile() for file in self.drag_and_drop_files}
            self.drag_and_drop_files = list()
        else:
            # 用户通过对话框选择文件
            new_files = set(QFileDialog.getOpenFileNames(self, '选择文件', '*')[0])

        # 计算尚未添加到列表的新文件
        files_to_add = new_files - current_files
        if files_to_add:
            self.list_widget_file.addItems(files_to_add)

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

    # 在 MainWindow 类中重写 closeEvent 方法
    def closeEvent(self, event):
        self.controller.minimize_wx()  # 最小化微信
        self.controller.thread_pool.waitForDone()  # 等待所有线程完成
        event.accept()

    def show_message_box(self, title, message, level='warning'):
        if level == 'warning':
            QMessageBox.warning(self, title, message)
        else:
            QMessageBox.critical(self, title, message)

    def tray_icon_activated(self, reason):
        # 当系统托盘图标被激活时的操作
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.restore_from_tray()

    def restore_from_tray(self):
        # 还原窗口
        if self.flag:
            self.hide()
            self.flag = not self.flag
        else:
            self.showNormal()
            self.flag = not self.flag

    def create_actions(self):
        # 创建系统托盘图标菜单的动作
        self._restore_action = QAction("显示", self)
        self._restore_action.triggered.connect(self.restore_from_tray)  # "显示"菜单项触发还原窗口的操作

        self._quit_action = QAction("退出", self)
        self._quit_action.triggered.connect(lambda: os._exit(0))  # "退出"菜单项触发退出应用程序的操作

    def create_tray_icon(self):
        # 创建系统托盘图标的菜单
        self._tray_icon_menu = QMenu(self)
        self._tray_icon_menu.addAction(self._restore_action)
        self._tray_icon_menu.addSeparator()
        self._tray_icon_menu.addAction(self._quit_action)

        self.tray_icon.setContextMenu(self._tray_icon_menu)
        self.tray_icon.show()

    def listen_keyboard(self):
        # 键盘监听
        shortcut = QShortcut(QKeySequence("Esc"), self)
        # 当按下 Esc 键时隐藏窗口
        shortcut.activated.connect(self.restore_from_tray)

    def listen_keyboard_chain(self):
        # 创建系统托盘图标相关的变量和对象
        self._restore_action = QAction()
        self._quit_action = QAction()
        self._tray_icon_menu = QMenu()

        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        # self.tray_icon.setIcon(QIcon(u":resources/images/trash.png"))
        self.tray_icon.setIcon(QIcon(u":/trash.png"))
        self.tray_icon.setToolTip("辅助小工具")

        # 创建系统托盘图标的菜单和动作
        self.create_actions()
        self.create_tray_icon()
        self.tray_icon.show()

        # 连接系统托盘图标的激活信号到槽函数
        self.tray_icon.activated.connect(self.tray_icon_activated)

        # 键盘监听
        self.listen_keyboard()
