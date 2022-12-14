import json
import re

import requests

header = {'origin': 'https://www.bilibili.com', 'referer': 'https://www.bilibili.com',
          'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}


def get():
    with open('tmp/get_qr.json', 'r') as f:
        res = json.loads(f.read())
    f.close()
    oauthKey = res['oauthKey']
    url2 = f'http://passport.bilibili.com/qrcode/getLoginInfo?oauthKey={oauthKey}'
    requests_json = {"oauthKey": oauthKey, "gourl": "http://www.bilibili.com"}
    cookie_before = requests.post(url=url2, json=requests_json, headers=header).json()
    print(cookie_before)
    if 'code' in cookie_before:
        if cookie_before['code'] == 0:
            data = cookie_before['data']['url']
            DedeUserID = re.findall('DedeUserID=(.*?)&', data)[0]
            DedeUserID__ckMd5 = re.findall('DedeUserID__ckMd5=(.*?)&', data)[0]
            SESSDATA = re.findall('SESSDATA=(.*?)&', data)[0]
            bili_jct = re.findall('bili_jct=(.*?)&', data)[0]
            cookie = f'{{\"cookies\":{{\"DedeUserID\":\"{DedeUserID}\",\"DedeUserID__ckMd5\":\"{DedeUserID__ckMd5}\",\"SESSDATA\":\"{SESSDATA}\",\"bili_jct\":\"{bili_jct}\"}}}}'
            with open('UserData/cookies.json', 'w') as f:
                f.write(cookie)
            f.close()
            return 'Success'
        else:
            return 'False'
    else:
        return 'False'
