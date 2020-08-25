import requests
import json

def tuling_reply(url, apikey, msg):
    data = {     # 这个是在帮助手册上直接复制过来的
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "天坛北门"
                }
            }
        },
        "userInfo": {
            "apiKey": apikey,      # 你注册的apikey
            "userId": "anystr"      # 随便填点
        }
    }
    headers = {'content-type': 'application/json'}     # 必须是json
    r = requests.post(url, headers=headers, data=json.dumps(data))
    return r.json()

if __name__ == '__main__':
    apikey = '填入机器人的apikey'
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    while True:
        msg = input('(输入quit结束)> ').strip()
        if not msg:
            continue
        if msg == 'quit':
            break
        reply = tuling_reply(url, apikey, msg)
        print(reply["results"][0]["values"]["text"])    # 可以直接打印reply