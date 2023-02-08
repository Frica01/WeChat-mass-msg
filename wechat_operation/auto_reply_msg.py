# -*- coding: utf-8 -*-
# @Author : Frica01
# @Time   : 2022-12-15 13:56
# @Name   : auto_reply_msg.py

import time
import openai
import uiautomation as auto
from wx_operation import WxOperation

wx = WxOperation()


def get_records() -> list:
    """获取聊天记录"""
    records = wx.get_chat_records(page=0)
    if records.__len__() >= 5:
        records = records[-5:]
    print(records)
    return records


def get_response(msg: str):
    """获取回答的内容"""
    # Set your API key
    openai.api_key = "sk-你的的api_key"
    # Use the GPT-3 model
    msg += "，需要使用中文回答"
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=msg,
        max_tokens=1024,
        temperature=0.5
    )
    return '\n'.join(completion.choices[0].text.split('\n')[2:])


def reply(msg: str):
    auto.SetClipboardText(text=msg)
    wx.input_edit.SendKeys(text='{Ctrl}v', waitTime=0.1)
    wx.wx_window.SendKey(key=auto.SpecialKeyNames['ENTER'], waitTime=0.2)


def main(sleep_time: int):
    # 建立一个字典和列表
    records_map = dict()
    records_list = list()
    while True:
        # 获取聊天记录
        records = get_records()
        for item in records:
            # 如果不存在消息不是文本就跳过
            if item.get('type') != 'Content':
                continue
            # 需要@chatGPT 关键词来促发后面的操作
            if '@chatGPT' not in item.get('msg'):
                continue
            # 获取发送信息的人和内容
            name = item.get('name')
            content = item.get('msg').split('@chatGPT')[1]
            # 如果 同一个人+用一段文本 已经发送过，则跳过
            if name + '××÷÷' + content in records_list:
                continue
            records_list.append(name + '××÷÷' + content)
            # 如果该内容已经提问过，则从 records_map 取出来回答
            if records_map.get(content):
                reply(msg=records_map.get(content))
            # 如果该内容已经提问过，则从添加到 records_map
            else:
                response = '[回复]:\n' + get_response(msg=content)
                reply(msg=response)
                records_map[content] = response

            print(records_map[content])

        time.sleep(sleep_time)


if __name__ == '__main__':
    main(sleep_time=10)
