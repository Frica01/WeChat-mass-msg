# -*- coding: utf-8 -*-
# Name:         controller.py
# Author:       小菜
# Date:         2023/11/28 10:37
# Description:


import keyboard
from PySide6.QtCore import (QMutex, QWaitCondition, QMutexLocker, QObject, Signal)

from models.model import ModelMain
from views.main_window import ViewMian


class ControllerMain(QObject):
    progress_updated_signal = Signal(int, int)  # 进度条 signal

    def __init__(self):
        super().__init__()
        self.model = ModelMain()
        self.view = ViewMian()

        # 互斥锁 和 条件等待
        self.paused = False
        self.mutex = QMutex()
        self.pause_condition = QWaitCondition()

        # 进度条 signal 连接到 view.update_progress 函数
        self.progress_updated_signal.connect(self.view.update_progress)
        self.view.init_progress()
        self.view.btn_send.clicked.connect(self.on_send_clicked)
        self.view.btn_pause_or_continue.clicked.connect(self.toggle_pause)

        # 设置快捷键
        keyboard.add_hotkey('Ctrl+Alt+Q', self.view.restore_from_tray)

    def toggle_pause(self):
        """切换暂停状态"""
        self.paused = not self.paused
        with QMutexLocker(self.mutex):
            if not self.paused:
                self.pause_condition.wakeAll()
        # 切换按钮文本
        current_text = self.view.btn_pause_or_continue.text()
        self.view.btn_pause_or_continue.setText('暂停发送' if current_text == '继续发送' else '继续发送')

    def check_pause(self):
        """检查暂停"""
        if self.paused:
            with QMutexLocker(self.mutex):
                self.pause_condition.wait(self.mutex)

    def on_send_clicked(self):
        """点击发送"""
        # 获取 GUI 工具面板的信息
        data = self.view.get_data()
        # 开始发送，传递检查暂停函数和进度条信号
        self.model.run_send_msg(
            **data,
            check_pause=self.check_pause,
            progress_updated_signal=self.progress_updated_signal
        )
