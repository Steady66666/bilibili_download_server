import json

import requests
import cookies

header = {'origin': 'https://www.bilibili.com', 'referer': 'https://www.bilibili.com',
          'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}
cookie = cookies.cookies
csrf = cookies.bili_jct
url = 'https://api.bilibili.com/pgc/web/follow/del'


def del_drama(seaon_id):
    json_data = {"season_id": seaon_id, "csrf": csrf}
    # json_data = json.dumps(json_data)
    res = requests.post(url=url, data=json_data, headers=header, cookies=cookie).json()
    return res


# ress = del_drama('35870')
# print(ress)

