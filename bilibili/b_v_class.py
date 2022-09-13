import json

import dash
import download_info
from get_respones import get_response
from cookies import bili_jct

csrf = bili_jct


# 课程列表
def class_list():
    live_list_url = 'https://api.bilibili.com/pugv/pay/web/my/paid?ps=10&pn=1'  # 课程列表
    list_res = get_response(live_list_url).json()['data']['data']
    # print(list_res) 67 420
    list_res = json.dumps(list_res, ensure_ascii=False)
    return list_res
# {"code":0,"message":"success","data":{"data":[{"id":67,"title":"name"},{"id":68,"title":"name"}]}}


# 选中课程的dash信息
def class_info(class_id):
    obj_url = f'https://api.bilibili.com/pugv/view/web/season?season_id={class_id}&csrf={csrf}'
    res = get_response(obj_url).json()['data']
    # 题目
    Name = str(res['title']).replace(' ', '').replace('&amp;', '').replace('&lt;', '').replace('&#x27;', '').replace('&gt;', '').replace('&quot;', '').replace('&#770;', '').replace('&#771;', '').replace('|', '').replace('*', '').replace('?', '').replace(':', '').replace('/', '').replace('\\', '').replace('\"', '').replace('<', '').replace('>', '')
    obj_res_list = res['episodes']
    Eps = []
    for i in obj_res_list:
        name = str(i['title']).replace(' ', '').replace('&amp;', '').replace('&lt;', '').replace('&#x27;', '').replace('&gt;', '').replace('&quot;', '').replace('&#770;', '').replace('&#771;', '').replace('|', '').replace('*', '').replace('?', '').replace(':', '').replace('/', '').replace('\\', '').replace('\"', '').replace('<', '').replace('>', '')
        avid = i['aid']
        cid = i['cid']
        ep_id = i['id']
        dash_url = f'https://api.bilibili.com/pugv/player/web/playurl?avid={avid}&cid={cid}&qn=0&fnver=0&fnval=16&fourk=1&ep_id={ep_id}'
        class_subdata = {"ep_name": name, "url": dash_url}
        Eps.append(class_subdata)
    class_data = {"location": "class", "Name": Name, "Eps": Eps}
    download_info.data_download(class_data)
    # class_data = json.dumps(class_data, ensure_ascii=False)
    # return class_data


# {"location": "class", "Name": "《线性代数》2小时讲完附赠笔记", "Eps": [{"ep_name": "课时01行列式的性质与计算", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329939&cid=171995688&qn=0&fnver=0&fnval=16&fourk=1&ep_id=866"}, {"ep_name": "课时02行列式的展开", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329941&cid=137463831&qn=0&fnver=0&fnval=16&fourk=1&ep_id=867"}, {"ep_name": "课时03矩阵", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329942&cid=401422550&qn=0&fnver=0&fnval=16&fourk=1&ep_id=868"}, {"ep_name": "课时04万能的初等行变换", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329943&cid=185116763&qn=0&fnver=0&fnval=16&fourk=1&ep_id=869"}, {"ep_name": "课时05向量组", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329940&cid=137467609&qn=0&fnver=0&fnval=16&fourk=1&ep_id=870"}, {"ep_name": "课时06解方程组", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329937&cid=137458583&qn=0&fnver=0&fnval=16&fourk=1&ep_id=863"}, {"ep_name": "课时07特征值特征向量对角化", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329938&cid=137459960&qn=0&fnver=0&fnval=16&fourk=1&ep_id=864"}, {"ep_name": "课时08二次型", "url": "https://api.bilibili.com/pugv/player/web/playurl?avid=80329944&cid=137461636&qn=0&fnver=0&fnval=16&fourk=1&ep_id=865"}]}
# print(class_info(67))
# print(class_list())
