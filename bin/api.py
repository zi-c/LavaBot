# Lava Bot API
# 作者：ZiChen  时间：20250305
# 版本：1.0.0

import os
import json
import requests

# cq码清理工具
def cq_clean(text):

    while True:
        start_index = text.find("[CQ:")
        if start_index == -1:
            break
        end_index = text.find("]", start_index)
        if end_index == -1:
            break
        text = text[:start_index] + text[end_index + 1:]

    return text


# 发送私人消息
def send_private_msg(user_id,msg):

    global http_url

    send_url = http_url + "/send_private_msg?user_id=" + str(user_id) + "&message=" + msg
    response = requests.get(send_url)
    return response.text


# 发送群聊消息
def send_group_msg(group_id,msg):

    global http_url

    send_url = http_url + "/send_group_msg?group_id=" + str(group_id) + "&message=" + msg
    response = requests.get(send_url)
    return response.text


# 获取用户昵称
def get_nickname(user_id):

    global http_url

    send_url = http_url + "/get_stranger_info?user_id=" + str(user_id)

    response = requests.get(send_url)

    json_data_nickname = json.loads(response.text)

    # 如果获取成功
    if json_data_nickname.get("status") == "ok":
        nickname = json_data_nickname['data']['nick']
    else:
        nickname = "QQUser"

    return nickname