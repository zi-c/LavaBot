# Stat Plugin
# 作者：ZiChen  时间：20250306
# 版本：1.0.0

import lavabot
import os
import psutil
import requests
from urllib.parse import quote

# 当好友/群聊中有消息内容为（*stat）时，且发送者为主人QQ时，获取设备自身情况并发送到群里。

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
            if raw_message != '*stat':
                return()

            print(lavabot.cmd_time() + "Stat: 收到获取状态命令")

            # 如果成功获取相应 发送消息
            sent_msg = stat_msg(master_id)
            sent_msg = quote(sent_msg)  # 对消息进行 URL 编码
            response = lavabot.send_private_msg(user_id, sent_msg)
            print(lavabot.cmd_time() + "Stat: 消息已发送:", response)
            return()

        # 如果消息来源是群聊
        if message_type == "group":

            # 权限鉴定
            if user_id != master_id:
                return()
            if raw_message != '*stat':
                return()

            print(lavabot.cmd_time() + "Stat: 收到获取状态命令")

            # 如果成功获取相应 发送消息
            sent_msg = stat_msg(master_id)
            sent_msg = quote(sent_msg)  # 对消息进行 URL 编码
            response = lavabot.send_group_msg(group_id, sent_msg)
            print(lavabot.cmd_time() + "Stat: 消息已发送:", response)
            return()

    return()


# 获取CPU型号和核心数
def get_cpu_info():

    with open('/proc/cpuinfo', 'r') as cpuinfo:
        cpu_info = cpuinfo.readlines()

    # 获取CPU型号
    model_name = None
    for line in cpu_info:
        if "model name" in line:
            model_name = line.split(":")[1].strip()
            break

    # 获取CPU核心数
    logical_cores = psutil.cpu_count(logical=True)  # 逻辑核心数

    return model_name, logical_cores

# 获取CPU使用率
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)  # 1秒内的CPU使用率

# 获取内存使用量（百分比）
def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.percent  # 内存使用百分比

# 获取硬盘使用量（百分比）
def get_disk_usage():
    disk = psutil.disk_usage('/')  # 根目录的磁盘使用情况
    return disk.percent  # 磁盘使用百分比


def stat_msg(master_id):
    # 获取CPU信息
    cpu_model, logical_cores = get_cpu_info()
    # 获取CPU使用率
    cpu_usage = get_cpu_usage()
    # 获取内存使用量
    memory_usage = get_memory_usage()
    # 获取硬盘使用量
    disk_usage = get_disk_usage()

    # 处理文本
    stat_msg = ""
    stat_msg = stat_msg + f'\nCPU型号: {cpu_model}'
    stat_msg = stat_msg + f'\n逻辑核心数: {logical_cores}'
    stat_msg = stat_msg + f'\nCPU使用率: {cpu_usage}%'
    stat_msg = stat_msg + f'\n内存使用量: {memory_usage}%'
    stat_msg = stat_msg + f'\n硬盘使用量: {disk_usage}%'

    return(stat_msg)