from download_list import data_jsonfy
import os
import downloader


def download_class(base_path, dash_data, num=None):
    if not os.path.exists(base_path):  # 环境更改
        os.makedirs(base_path)
    os.chdir(base_path)

    if dash_data['type'] == 'single':  # 单个投稿视频
        d_path = f"{base_path}"
        play_json = data_jsonfy(dash_data, num)
        downloader.download(play_json['name'], play_json['a_url'], play_json['v_url'], d_path)
        return {"code": 0, "msg": "download complate!", "type": "bvideo"}

    elif dash_data['type'] == 'list':  # 投稿视频合集
        season_name = dash_data['Season_name']
        if not os.path.exists(season_name):
            os.makedirs(season_name)
        os.chdir(season_name)
        dashs_data = dash_data['Eps']
        for dash_data in dashs_data:
            play_json = data_jsonfy(dash_data, num)
            d_path = f'{base_path}/{season_name}'
            downloader.download(play_json['name'], play_json['a_url'], play_json['v_url'], d_path)
            return {"code": 0, "msg": "download complate!", "type": "bvideo"}
