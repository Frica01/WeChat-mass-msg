# -*- coding: utf-8 -*-
# Name:         controller.py
# Author:       小菜
# Date:         2023/11/28 10:37
# Description:


from PySide6.QtCore import (QRunnable, QThreadPool, QMutex, QWaitCondition, QMutexLocker, QObject, Signal)


class WxOperationRunnable(QRunnable):
    def __init__(self, controller, model, *args, **kwargs):
        super().__init__()
        self.controller = controller
        self.model = model
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.controller.check_pause()
        self.model.send_message(*self.args, **self.kwargs)
        self.controller.task_completed()  # 通知控制器任务完成


class WxController(QObject):
    progress_updated = Signal(int, int)

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.minimize_wx = model.wx_operation.minimize_wx
        #
        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)
        #
        self.paused = False
        self.mutex = QMutex()
        self.pause_condition = QWaitCondition()
        #
        self.completed_tasks = 0
        self.total_tasks = 0

    # @property
    def has_wx_instance(self) -> bool:
        """判断微信是否存在"""
        if hasattr(self.model, 'wx_operation'):
            return True
        return False

    def toggle_pause(self):
        self.paused = not self.paused
        with QMutexLocker(self.mutex):
            if not self.paused:
                self.pause_condition.wakeAll()

    def check_pause(self):
        if self.paused:
            with QMutexLocker(self.mutex):
                self.pause_condition.wait(self.mutex)

    def start_sending_messages(self, msgs, newline_msg, add_remark_name, files, friends, is_specify_tag,
                               is_specify_group):
        if is_specify_group:
            friends = [friend for friend in friends.split()]
        # 判断是否点击标签
        elif is_specify_tag:
            friends = self.model.get_tag_friend_list(friends)
        else:
            friends = [friend for friend in friends.split()]

        self.completed_tasks = 0
        self.total_tasks = len(friends)
        self.progress_updated.emit(self.completed_tasks, self.total_tasks)
        for idx, friend in enumerate(friends):
            runnable = WxOperationRunnable(self, self.model, msgs, newline_msg, files, friend, add_remark_name)
            self.thread_pool.start(runnable)

    def task_completed(self):
        # 每完成一个任务，计数器加一
        self.completed_tasks += 1
        self.progress_updated.emit(self.completed_tasks, self.total_tasks)
