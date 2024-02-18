# -*- coding: utf-8 -*-
# Name:         utils.py
# Author:       小菜
# Date:         2024/2/18 15:30
# Description:

import psutil


def get_specific_process(proc_name: str = 'WeChat.exe') -> bool:
    """获取指定进程是否存在"""
    return any(proc.name() == proc_name for proc in psutil.process_iter(attrs=['name']))
