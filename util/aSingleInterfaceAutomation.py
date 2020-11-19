'''
接口自动化函数
传入
'''

import requests

def requestInterface(url, method, headers, data):
    # 请求接口
    if method == 'post':
        json = requests.post(url).text.encode('utf-8').decode('unicode_escape')
        return json
    if method == 'get':
        json = requests.get(url).text.encode('utf-8').decode('unicode_escape')
        return json
