# Lava Bot (Beta)
# 作者：ZiChen  时间：20250523
# 版本：0.1.0

import websocket
import re
import json
import array as arr
from datetime import datetime
import concurrent.futures

# 当前版本为体验版，部分功能细节已删除。
# 请编辑 /bin/config.py 修改配置，并修改Plugins里的相关配置信息。
# 欢迎加入梓宸的交流群：120361305

# 基础服务参数
global ws_url
global http_url


with open("bin/config.py", "r", encoding="utf-8") as file0:
    exec(file0.read())  # 载入配置
with open("bin/api.py", "r", encoding="utf-8") as file1:
    exec(file1.read())  # 载入API
with open("bin/json.py", "r", encoding="utf-8") as file2:
    exec(file2.read())  # 载入解析器


if aichat_set == True:
    from plugins import aichat
if pingpong_set == True:
    from plugins import pingpong
if stat_set == True:
    from plugins import stat
if headhunts_set == True:
    from plugins import headhunts

# 创建线程池
Thread_Pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)


# 获取当前时间
def cmd_time():
    now = datetime.now()
    formatted_time = now.strftime("<%Y-%m-%d %H:%M:%S> ") # 格式化输出
    return formatted_time


# 定义WebSocket回调类
class MyWebSocket:

    def on_open(self, ws):
        print(cmd_time() + "System: 连接已打开")

    def on_message(self, ws, message):
        #print(cmd_time() + "System: 收到消息")
        #print(cmd_time() + "System: 收到消息:", message)

        # 处理消息(多线程)
        Thread_Pool.submit(aichat.core, message)
        Thread_Pool.submit(pingpong.core, message)
        Thread_Pool.submit(stat.core, message)
        Thread_Pool.submit(headhunts.core, message)

    def on_error(self, ws, error):
        print(cmd_time() + "System: 发生错误:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print(cmd_time() + "System: 连接已关闭")


# 主程序(WS)
def main():
    global ws_url
    ws_app = websocket.WebSocketApp( ws_url, on_open=MyWebSocket().on_open, on_message=MyWebSocket().on_message, on_error=MyWebSocket().on_error, on_close=MyWebSocket().on_close )
    ws_app.run_forever()


if __name__ == "__main__":
    print(cmd_time() + "System: 欢迎使用Lava Bot，服务正在启动中！")
    main()