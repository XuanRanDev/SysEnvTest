import os

import requests

env = os.environ


# PushPlus
def pushMessage(info):
    url = 'http://www.pushplus.plus/send?token=' + '1f630c6f480246a2b174dfedb49be0fa' + '&title=' + info + '&content=' + info + '&template=html'
    resp = requests.post(url)
    if resp.json()["code"] == 200:
        print('推送消息提醒成功！')
    else:
        print('推送消息提醒失败！')


if __name__ == '__main__':
    info = os.environ.get("USERS", "")
    print(os.environ.get("USERS", "1"))
    pushMessage(info)
