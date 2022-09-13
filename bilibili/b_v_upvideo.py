import json
import re

from get_respones import get_response


def upvideo(upurl):
    up_vmid = str(re.findall('com/(.*?)\?', upurl)[0])
    pn = 0
    up_name = str(re.findall('<title>(.*?)的个人空间_哔哩哔哩_Bilibili</title>', get_response(upurl).text)[0])
    path_up = str(up_name) + '_' + str(up_vmid)  # up信息
    pages_url = f'https://api.bilibili.com/x/space/arc/search?mid={up_vmid}&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
    pages = int((int(json.loads(get_response(pages_url).text)['data']['page']['count']) + 30) / 30)
    vvlist = ''
    while pn < pages:
        pn = pn + 1
        url = f'https://api.bilibili.com/x/space/arc/search?mid={up_vmid}&ps=30&tid=0&pn={pn}&keyword=&order=pubdate&jsonp=jsonp'
        res = json.loads(get_response(url).text)['data']['list']['vlist']
        for bvid_data in res:
            title = str(bvid_data['title'])
            bvid = str(bvid_data['bvid'])
            vlist = f"{{\'name\':\'{title}\', \'url\':\'https://www.bilibili.com/video/{bvid}?\'}}"
            vvlist = vvlist + ',' + vlist
    vlist = vvlist[1:]
    all_up_vs = f"{{\'up_name\':\'{path_up}\', \'vlist\':[{vlist}]}}"
    all_up_data = json.dumps(eval(all_up_vs), ensure_ascii=False)
    return all_up_data
# 后面的函数转递给  b_v_bvideo.py   由其生成dash数据  bviedio(url)


# upvideo('https://space.bilibili.com/1084672528?spm_id_from=333.1007.tianma.1-1-1.click')
# print(upvideo('https://space.bilibili.com/1084672528?spm_id_from=333.1007.tianma.1-1-1.click'))
