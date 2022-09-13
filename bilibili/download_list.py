
def data_jsonfy(data, num=None):  # 返回最优匹配选项地址：音频、视频
    print(num)
    ep_name = data['ep_name']
    dash_data = data['dash']
    flac_statu = 'flac' in dash_data
    print(f'flac模式存在：{flac_statu}')
    if 'flac' in dash_data:
        if dash_data['dolby'] is None and dash_data['flac'] is None:
            a_url = [dash_data['audio'][0]['base_url'], dash_data['audio'][0]['backup_url'][0],
                     dash_data['audio'][0]['backup_url'][1]]
        elif dash_data['dolby']:
            if dash_data['dolby']['audio']:
                a_url = [dash_data['dolby']['audio'][0]['base_url'], dash_data['dolby']['audio'][0]['backup_url'][0],
                         dash_data['dolby']['audio'][0]['backup_url'][1]]
            else:
                a_url = [dash_data['audio'][0]['base_url'], dash_data['audio'][0]['backup_url'][0],
                         dash_data['audio'][0]['backup_url'][1]]
        elif dash_data['flac']:
            a_url = [dash_data['flac']['audio']['base_url'], dash_data['flac']['audio']['backup_url'][0],
                     dash_data['flac']['audio']['backup_url'][1]]
    else:
        if dash_data['dolby'] is None:
            a_url = [dash_data['audio'][0]['base_url'], dash_data['audio'][0]['backup_url'][0],
                     dash_data['audio'][0]['backup_url'][1]]
        elif dash_data['dolby']:
            if dash_data['dolby']['audio']:
                a_url = [dash_data['dolby']['audio'][0]['base_url'], dash_data['dolby']['audio'][0]['backup_url'][0],
                         dash_data['dolby']['audio'][0]['backup_url'][1]]
            else:
                a_url = [dash_data['audio'][0]['base_url'], dash_data['audio'][0]['backup_url'][0],
                         dash_data['audio'][0]['backup_url'][1]]
    v_url = []
    if num:
        for i in dash_data['video']:
            # print(i['id'])
            obj_id = int(i['id'])
            if type(num) != type(1):
                num = int(num)
            if obj_id == num:
                print('匹配到清晰度')
                v_url = [i['base_url'], i['backup_url'][0], i['backup_url'][1]]
                break
    if not num:
        print('没有匹配到清晰度')
        i = dash_data['video'][0]
        v_url = [i['base_url'], i['backup_url'][0], i['backup_url'][1]]
    json_info = {"name": ep_name, "v_url": v_url, "a_url": a_url}
    return json_info
