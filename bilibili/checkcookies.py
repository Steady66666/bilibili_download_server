import json

from get_respones import get_response


# 检测cookie是否失效
def check_cookie():
    check_url = f'https://account.bilibili.com/site/getCoin'
    check_result = get_response(check_url).json()
    if check_result['code'] == 0:
        coin_num = check_result['data']['money']
        print(f'Cookie有效，目前硬币为:{coin_num}')
        info = {"code": 0, "status": "true", "data": {"money": coin_num}}
        info = json.dumps(info)
        return info
    else:
        print('Cookie失效！！！')
        info = {"code": -1, "status": "false", "data": None}
        info = json.dumps(info)
        return info
# print(check_cookie())
