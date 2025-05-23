# Arknights HeadHunts Simulate Plugin
# 作者：ZiChen  时间：20250414
# 版本：1.0.0

from urllib.parse import quote
import requests
import lavabot

# 当群聊中有消息内容为（明日方舟寻访模拟）时，调用寻访接口获取寻访图并发送到群中。
# 接口调用来源：ZiChen API，如果失效请更换为其他接口，请勿滥用。

def core(data):

    message_type, bot_id, user_id, group_id, message_id, raw_message = lavabot.read_json(data)
    if message_type and user_id and raw_message:
        if message_type == "group":
            if raw_message != '明日方舟寻访模拟':
                return()
            print(lavabot.cmd_time() + "HeadHunts: 收到寻访模拟命令")
            if raw_message:
                ai_msg_img = quote(f"[CQ:image,file=https://app.zichen.zone/api/headhunts/api.php?type=img&from=lavabot]")
                response = lavabot.send_group_msg(group_id, ai_msg_img)
                print(lavabot.cmd_time() + "HeadHunts: 消息已发送:", response)

    return()