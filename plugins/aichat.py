# AIChat Plugin
# 作者：ZiChen  时间：20250523

import lavabot
import time
import random
from openai import OpenAI
from urllib.parse import quote

# 请设置API Key，否者无法使用（第59行）
# 当群中有@机器人且带内容时，将调用接口并进行回复。

def core(data):

	# 解析接收到的消息
	message_type, bot_id, user_id, group_id, message_id, raw_message = lavabot.read_json(data)

	if message_type and user_id and raw_message:

		if message_type == "group":

			if ("[CQ:at,qq=" + bot_id + "]") in raw_message:

				raw_message = raw_message.replace("[CQ:at,qq=" + bot_id + "]", "")
				raw_message = raw_message.replace(" ", "")

				raw_message = lavabot.cq_clean(raw_message)
				if raw_message == "":
					return()

				user_name = lavabot.get_nickname(user_id)
				ai_msg = chat_api(raw_message, user_name, user_id)

				if ai_msg:
					sent_msg = f'{ai_msg}'
					sent_msg = quote(sent_msg)  # 对消息进行 URL 编码
					response = lavabot.send_group_msg(group_id, sent_msg)


					print(lavabot.cmd_time() + "AIChat: 消息已发送")
					return()
				else:
					print(lavabot.cmd_time() + "AIChat: 大模型调用失败")
					return()

	return()


# 调用大模型API
def chat_api(msg_txt, user_name, user_id):

	print(lavabot.cmd_time() + "AIChat: 正在调用 DeepSeek Api")
	print(lavabot.cmd_time() + f"AIChat: Msg:{user_name}：{msg_txt}")

	# 设置相关参数
	api_url = 'https://api.deepseek.com'
	# 获取 API Key
	# https://platform.deepseek.com/
	api_key = ''	
	if api_key = '':
		return("未设置接口钥匙")

	model_set = "deepseek-reasoner"
	prompt = '你的名字叫Lava，你在QQ群聊中，可以使用emoji在聊天内容中，尽量的简洁但具有情感，不要长篇大论。'

	client = OpenAI(api_key = api_key, base_url = api_url)

	response = client.chat.completions.create(
		# 随机选取模型
		model = model_set,
		messages=[
			{"role": "system", "content": prompt},
			{"role": "user", "content": f"昵称：{user_name}-QQ：{user_id}-发来消息说：{msg_txt}"}
		],
		stream=False,
		temperature = 1.0,
		max_tokens = 150
	)

	ai_response = response.choices[0].message.content

	if ai_response:
		print(lavabot.cmd_time() + f"AIChat: ID:{chat_id} AI:{ai_response}")
		return(ai_response)
	else:
		ai_response = '状态不佳，请帮我呼叫主人~'
		print(lavabot.cmd_time() + f"AIChat: ID:{chat_id} AI:{ai_response}")
		return(ai_response)

