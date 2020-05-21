# -*- encoding: utf-8 -*-

# 模拟发送post请求
import requests, json

url_json = 'http://192.168.150.240:11129/iapp/serviceSubmit'
data_json = json.dumps({'userNumber': '13005438277', 'messageContent': 'hello world'})

r_json = requests.post(url_json, data_json)
print(r_json)
print(r_json.text)
print(r_json.content)
