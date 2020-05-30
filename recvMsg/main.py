# 导入模块
import requests
import json

# 基础变量声明
formData = {
    'roomid': '21020284',
    'csrf_token': 'edd2efb8a13decada8860e627ea85e72',
    'csrf': 'edd2efb8a13decada8860e627ea85e72'
}
lastMsg = None


# 接收弹幕
def recvMsg():
    recv = requests.post("https://api.live.bilibili.com/ajax/msg", formData)
    username = json.loads(recv.text)['data']['room'][-1]['nickname']
    msg = json.loads(recv.text)['data']['room'][-1]['text']
    sendTime = json.loads(recv.text)['data']['room'][-1]['timeline']
    return username, msg, sendTime


while True:
    username, msg, sendTime = recvMsg()
    if (msg != lastMsg):
        print("[" + sendTime + "]-->" + username + "：" + msg)
        lastMsg = msg