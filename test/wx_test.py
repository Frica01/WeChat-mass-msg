# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2024-03-17 3:20
# @Name   : wx_test.py


from wechat_operation.wx_operation import WxOperation

wx = WxOperation()


def single_msg(name, msg, file_paths):
    wx.send_msg(name, msg, file_paths)


def mass_msg():
    ...


if __name__ == '__main__':
    single_msg('文件传输助手', ['123'], [])
