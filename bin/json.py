# Lava Bot 解析器
# 作者：ZiChen  时间：20250305
# 版本：1.0.0

# 载入解析器
import lavabot

def read_json(json_txt):

    try:

        json_data = json.loads(json_txt)
        if json_data.get("post_type") == "meta_event":
            return None, None, None, None, None, None

        # 如果为私聊消息
        if json_data.get('message_type') == "private":
            # 提取 bot_id user_id raw_message
            bot_id = str(json_data['self_id'])          #机器人ID
            user_id = str(json_data['user_id'])         #发送者ID
            message_id = str(json_data['message_id'])   #消息ID
            raw_message = json_data['raw_message']      #消息内容

            return "private", bot_id, user_id, None, message_id, raw_message

        # 如果为群聊消息
        if json_data.get('message_type') == "group":
            # 提取 bot_id group_id raw_message
            bot_id = str(json_data['self_id'])              #机器人ID
            user_id = str(json_data['sender']['user_id'])   #发送者ID
            group_id = str(json_data['group_id'])           #群聊ID
            message_id = str(json_data['message_id'])       #消息ID
            raw_message = json_data['raw_message']          #消息内容

            return "group" , bot_id, user_id, group_id, message_id, raw_message

        return None, None, None, None, None, None


    except json.JSONDecodeError:

        print(lavabot.cmd_time() + "BOT: 解析消息失败 JSON 格式错误")
        return None, None, None, None, None, None