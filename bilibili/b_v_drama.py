# 1为追番剧 2为追剧
# 需要改路径
import json
import time

import download_info
import unfollow
from get_respones import get_response
from cookies import dedeuserid


# 获取追剧列表
def series_list(drama_type):
    if drama_type == 1:
        location = 'cartoon'
    elif drama_type == 2:
        location = 'drama'
    pn = 0
    info = []
    while True:
        pn = pn + 1
        millis = int(round(time.time() * 1000))
        url = f'https://api.bilibili.com/x/space/bangumi/follow/list?type={drama_type}&follow_status=0&pn={pn}&ps=30&vmid={dedeuserid}&ts={millis}'  # 获取50个剧集信息
        series_list_info = get_response(url).json()['data']['list']
        if not series_list_info:
            info = json.dumps(info, ensure_ascii=False)
            return info
        for single in series_list_info:
            media_id = single['media_id']
            season_type_name = single['season_type_name']
            id_url = f'https://api.bilibili.com/pgc/review/user?media_id={media_id}'
            ep_json = get_response(id_url).json()
            ep_id = ep_json['result']['media']['new_ep']['id']
            season_id = ep_json['result']['media']['season_id']
            status = ep_json['result']['media']['new_ep']['index_show']
            title = single['title'] + '--' + single['season_title']
            sinfo = {"location": location, "block": season_type_name, "Name": title, "status": status, "media_id": media_id,
                     "ep_id": ep_id, "season_id": season_id}
            info.append(sinfo)


def seasons_info(drama_data):  # 9/4 此为后端操作
    ep_id = drama_data['ep_id']
    ep_url = f'https://api.bilibili.com/pgc/view/web/season?ep_id={ep_id}'
    location = drama_data['location']
    block = drama_data['block']
    status = drama_data['status']
    season_id = drama_data['season_id']
    Name = str(drama_data['Name']).replace(' ', '').replace('&amp;', '').replace('&lt;', '').replace('&#x27;',
                                                                                                     '').replace('&gt;',
                                                                                                                 '').replace(
        '&quot;', '').replace('&#770;', '').replace('&#771;', '').replace('|', '').replace('*', '').replace('?',
                                                                                                            '').replace(
        ':', '').replace('/', '').replace('\\', '').replace('\"', '').replace('<', '').replace('>', '')
    vs_info = get_response(ep_url).json()
    finished = vs_info['result']['publish']['is_finish']  # 完结与否 0或者1
    vs_info = vs_info['result']['episodes']
    dash_info = []
    for v_info in vs_info:
        ep_name = str(v_info['share_copy']).replace(' ', '').replace('&amp;', '').replace('&lt;', '').replace('&#x27;',
                                                                                                              '').replace(
            '&gt;', '').replace('&quot;', '').replace('&#770;', '').replace('&#771;', '').replace('|', '').replace('*',
                                                                                                                   '').replace(
            '?', '').replace(':', '').replace('/', '').replace('\\', '').replace('\"', '').replace('<', '').replace('>',
                                                                                                                    '')
        aid = v_info['aid']
        cid = v_info['cid']
        ep_id = v_info['id']
        dash_url = f'https://api.bilibili.com/pgc/player/web/playurl?avid={aid}&cid={cid}&fnver=0&fnval=4048&fourk=1&ep_id={ep_id}'
        dash = {"ep_name": ep_name, "url": dash_url}
        dash_info.append(dash)
    info = {"location": location, "block": block, "Name": Name, "is_finish": finished, "status": status, "Eps": dash_info}
    download_info.data_download(info)
    if finished == 1:
        upload_json = unfollow.del_drama(season_id)
        upload_json = json.dumps(upload_json)
        return upload_json
    else:
        return {"code": 0, "msg": "未完结，不取消追番"}

# print(seasons_info({"location": "cartoon", "block": "番剧", "Name": "极主夫道--TV", "status": "全10话", "media_id": 28233902, "ep_id": 424914}))
# print(series_list(2))
