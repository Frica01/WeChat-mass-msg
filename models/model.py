# -*- coding: utf-8 -*-
# Name:         model.py
# Author:       小菜
# Date:         2023/11/28 10:37
# Description:


from PySide6.QtCore import (QRunnable, QThreadPool, Signal, Slot, QObject)

from wechat_operation.wx_operation import WxOperation

# 实例化 WxOperation
try:
    wx_operation = WxOperation()
except AssertionError:
    pass


def send_message(friend, msgs, newline_msg, files, add_remark_name):
    # 包装 wx_operation 的逻辑
    msgs_list = list()
    if msgs:
        msgs_list = [msg for msg in msgs.split('\n')]
    if newline_msg:
        msgs_list.extend(['\n'.join(newline_msg.split('\n'))])
    # 这里可以添加错误处理、日志记录等
    try:
        wx_operation.send_msg(friend, msgs=msgs_list, file_paths=files, add_remark_name=add_remark_name)
        return True
    except Exception as e:
        print(f"{friend}  ==> 发送消息时出现错误: {e}")
        return False


class WorkerRunnable(QRunnable):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        #
        self.friends = kwargs.get('friends')
        self.check_pause = kwargs.get('check_pause')
        self.task_status_signal = kwargs.get('task_status_signal')
        self.progress_updated_signal = kwargs.get('progress_updated_signal')

    def run(self):
        for idx, friend in enumerate(self.friends):
            self.check_pause()
            try:
                send_message(friend, *self.args)
            except AssertionError:
                self.task_status_signal.emit(True)
                return
            self.progress_updated_signal.emit(idx + 1, len(self.friends))  # 通知控制器任务完成
        self.task_status_signal.emit(True)


class ModelMain(QObject):
    task_status_signal = Signal(bool)

    def __init__(self):
        super().__init__()
        # 线程池
        self.thread_pool = QThreadPool()
        self.thread_pool.setMaxThreadCount(1)
        # 任务状态, 保证同时只有一个任务在执行
        self.task_status = False
        self.task_status_signal.connect(self.change_task_status)

    def run_send_msg(self, msgs, newline_msg, add_remark_name, files, friends, is_specify_tag,
                     is_specify_group, check_pause, progress_updated_signal):
        if self.task_status:
            return
        self.task_status = True
        if is_specify_group:
            friends = [friend for friend in friends.split()]
        # 判断是否点击标签
        elif is_specify_tag:
            friends = wx_operation.get_friend_list(tag=friends)
        else:
            friends = [friend for friend in friends.split()]
        progress_updated_signal.emit(0, len(friends))
        runnable = WorkerRunnable(
            msgs, newline_msg, files, add_remark_name,
            friends=friends,
            check_pause=check_pause,
            progress_updated_signal=progress_updated_signal,
            task_status_signal=self.task_status_signal
        )
        self.thread_pool.start(runnable)

    @Slot(bool)
    def change_task_status(self, item):
        self.task_status = False
