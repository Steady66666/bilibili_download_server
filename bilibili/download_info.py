# 需要改路径 ../donwload         ../tmp
# 需要传入json数据
# data_download(data, num=None) 请求方式
import json
import os.path
import bvideo_download
import class_download
import drama_download

base_path = os.getcwd()  # 默认路径


def data_download(data, num=None):
    data = str(data).replace('null', 'None').replace('true', '\"true\"')
    dash_data = json.loads(json.dumps(eval(data)))

    location = dash_data['location']
    print(location)
    if location == 'bvideo':
        download_path = f'{base_path}/download/{location}'
        res = bvideo_download.download_class(download_path, dash_data, num)
        return res

    elif location == 'class':  # API方式dash请求下载
        download_path = f'{base_path}/download/{location}'
        res = class_download.download_class(download_path, dash_data)
        return res

    elif location == 'cartoon':  # API方式dash请求下载
        download_path = f'{base_path}/download/{location}'
        res = drama_download.download_viedeo(download_path, dash_data)
        return res

    elif location == 'drama':
        download_path = f'{base_path}/download/{location}'
        res = drama_download.download_viedeo(download_path, dash_data)
        return res
    else:
        print('错误下载请求')
        return {"code": -1, "msg": False}

# data_download('极主夫道--TV')
# # print(res)
