# 2022/9/4 00：44 功能满足
# 主函数为bviedio()
from get_respones import get_response
import re
import json


def get_video_info(url):  # 播放dash
    response = get_response(url)
    json_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]  # json在html里面
    title = re.findall('<meta data-vue-meta="true" itemprop="name" name="title" content="(.*?)"><meta data-vue-meta=', response.text)
    if str(title) == "[]":
        title = '未知标题'
    else:
        title = title[0]
    title = str(title).replace('#', ' ').replace('.', '').replace(' ', '').replace('&amp;', '').replace('&lt;', '').replace('&#x27;', '').replace('&gt;', '').replace('&quot;', '').replace('&#770;', '').replace('&#771;', '').replace('', '').replace('|', '').replace('*', '').replace('?', '').replace(':', '').replace('/', '').replace('\\', '').replace('\"', '').replace('<', '').replace('>', '')
    json_data = json.loads(json_data)  # 视频信息格式化
    dash = str(json_data['data']['dash']).replace('null', 'None')
    return f"{{'ep_name':\'{title}\', 'dash':{dash}}}"


def video(url):
    info = get_video_info(url)
    return "{'location':'bvideo','type': 'single'," + info[1:]


def video_list(url):
    response = get_response(url)
    title = re.findall('<meta data-vue-meta="true" itemprop="name" name="title" content="(.*?)"><meta data-vue-meta=', response.text)
    if str(title) == "[]":
        title = '未知标题'
    else:
        title = title[0]
    totaltitle = str(title).replace('#', ' ').replace('.', '').replace(' ', '').replace('|', '').replace('*', '').replace('?', '').replace(':', '').replace('/', '').replace('\\', '').replace('\"', '').replace('<', '').replace('>', '')  # 视频总标题
    list_no = re.findall('<h3>视频选集</h3><span class="cur-page">((.*?))</span>', response.text)[0]
    list_no = str(list_no)
    list_no = int(re.findall(r"\d+", list_no)[1])
    print('查询到共有：'+str(list_no)+'个视频')
    url = str(re.findall('(.*?)\?', url)[0])
    s_video_info = ''
    for i in range(list_no):
        i = i+1
        print('正在处理第'+str(i)+'个视频')
        new_url = url + "?p=" + str(i)
        video_info = get_video_info(new_url)
        s_video_info = s_video_info + ',' + video_info
    s_video_info = s_video_info[1:]
    output_info = f"{{\'location\': \'bvideo\', \'type\': \'list\', \'Season_name\':\'{totaltitle}\', \'Eps\':[{s_video_info}]}}"
    return output_info


def bviedio(url):  # 是否为视频列表
    if str(re.findall('<h3>视频选集</h3><span class="cur-page">((.*?))</span>', get_response(url).text)) == '[]':
        return video(url)
    else:
        print('该链接中视频为列表，现进行列表下载————>>')
        return video_list(url)


# print(bviedio('https://www.bilibili.com/video/BV1sP411V7Em?spm_id_from=333.999.0.0'))
