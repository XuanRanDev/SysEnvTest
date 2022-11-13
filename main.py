import os
import requests
env = os.environ
print(os.environ.get("USERS", ""))
pushMessage()



# PushPlus
def pushMessage():
    url = 'http://www.pushplus.plus/send?token=' + '1f630c6f480246a2b174dfedb49be0fa' + '&title=' + os.environ.get("USERS", ""  + '&content=' + os.environ.get("USERS", "" + '&template=html'
    resp = requests.post(url)
    if resp.json()["code"] == 200:
        print('推送消息提醒成功！')
    else:
        print('推送消息提醒失败！')

