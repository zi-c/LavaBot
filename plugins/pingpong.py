# PingPong Plugin
# 作者：ZiChen  时间：20250305
# 版本：1.0.0

import lavabot
from urllib.parse import quote

# 当好友/群聊中有消息内容为（*ping）时，且发送者为主人QQ时，回复（Pong！）

def core(data):

    # 主人QQ
    master_id = '3328205609'
    
    message_type, bot_id, user_id, group_id, message_id, raw_message = lavabot.read_json(data)
    if message_type and user_id and raw_message:

        # 如果消息来源是私聊
        if message_type == "private":

            # 权限鉴定
            if user_id != master_id:
                return()
            if raw_message != '*ping':
                return()

            print(lavabot.cmd_time() + "Stat: 收到PingPong命令")
            if raw_message:
                sent_msg = quote('Pong！') # 对消息进行 URL 编码
                response = lavabot.send_private_msg(user_id, sent_msg)
                print(lavabot.cmd_time() + "PingPong: 消息已发送:", response)
                return()

        # 如果消息来源是群聊
        if message_type == "group":

            # 权限鉴定
            if user_id != master_id:
                return()
            if raw_message != '*ping':
                return()

            print(lavabot.cmd_time() + "Stat: 收到PingPong命令")
            if raw_message:
                sent_msg = quote('Pong！') # 对消息进行 URL 编码
                response = lavabot.send_group_msg(group_id, sent_msg)
                print(lavabot.cmd_time() + "PingPong: 消息已发送:", response)
                return()

    return()