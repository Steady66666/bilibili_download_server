from download_list import data_jsonfy
import os
import dash
import downloader


def download_viedeo(base_path, dash_data):
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    os.chdir(base_path)

    block_name = dash_data['block']
    if not os.path.exists(block_name):
        os.makedirs(block_name)
    os.chdir(block_name)
    season_name = dash_data['Name']
    if not os.path.exists(season_name):
        os.makedirs(season_name)
    os.chdir(season_name)
    dashs_data = dash_data['Eps']  # 此处开始导入dash函数 ##############################################
    for dash_url in dashs_data:
        dash_data = dash.get_dash_data(dash_url['url'])
        dash_data = {"ep_name": dash_url['ep_name'], "dash": dash_data}
        play_json = data_jsonfy(dash_data)
        d_path = f"{base_path}/{block_name}/{season_name}"
        downloader.download(play_json['name'], play_json['a_url'], play_json['v_url'], d_path)
    os.chdir(base_path)
    return {"code": 0, "msg": "download complate!", "type": "drama"}
