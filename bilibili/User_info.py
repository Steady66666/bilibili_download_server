import json
import re
import datetime
import get_respones
from cookies import dedeuserid
import time
# url = 'http://api.bilibili.com/x/member/web/account'
# url = 'https://api.bilibili.com/x/web-interface/nav'
# url = f'http://api.bilibili.com/x/safecenter/login_notice?mid={dedeuserid}'  # 登录地址


def yourinfo():
    # 需求：名称，mid，硬币，大会员，大会员到期时间，注册时间
    url = f"http://api.bilibili.com/x/space/acc/info?mid={dedeuserid}"  # [data]mid,name,sex,face,sign,level,silence,coins
    res = get_respones.get_response(url).json()['data']

    timearray = time.localtime(float(res['vip']['due_date']/1000))
    due_date = time.strftime("%Y-%m-%d %H:%M:%S", timearray)  # 大会员过期时间  2023-08-12 00:00:00
    mid = res['mid']
    name = res['name']
    coins = res['coins']
    vip = res['vip']['label']['text']
    # 注册时间   2019-08-25
    join_time = get_respones.get_response('https://member.bilibili.com/x/web/index/scrolls').json()['data']['scrolls'][0]['name']
    join_time = re.findall('第(.*?)天', join_time)[0]
    join_time = (datetime.datetime.now() - datetime.timedelta(days=int(join_time))).strftime("%Y-%m-%d")
    info = {"name": name, "mid": mid, "coins": coins, "vip": vip, "due_date": due_date, "join_time": join_time}
    info = json.dumps(info, ensure_ascii=False)
    return info

