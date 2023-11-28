# -*- coding: utf-8 -*-
# Name:         model.py
# Author:       小菜
# Date:         2023/11/28 10:37
# Description:

# wechat_operation/model.py
from wechat_operation.wx_operation import WxOperation


class WxModel:
    def __init__(self):
        self.wx_operation = WxOperation()

    def send_message(self, msgs, newline_msg, files, friend, add_remark_name):
        # 包装 wx_operation 的逻辑
        msgs_list = list()
        if msgs:
            msgs_list = [msg for msg in msgs.split('\n')]
        if newline_msg:
            msgs_list.extend(['\n'.join(newline_msg.split('\n'))])
        # 这里可以添加错误处理、日志记录等
        try:
            self.wx_operation.send_msg(friend, msgs=msgs_list, file_paths=files, add_remark_name=add_remark_name)
            return True
        except Exception as e:
            print(f"{friend}  ==> 发送消息时出现错误: {e}")
            return False

    def get_tag_friend_list(self, tag: str):
        return self.wx_operation.get_friend_list(tag=tag)
