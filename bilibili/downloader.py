# 三个传参，name,[v_url],[a_url]  需要添加传参：绝对路径
# 无需改路径
import os
import time
import subprocess
import get_respones


def chips(file_name, url):
    times = 0
    while times <= 2:
        try:
            res = get_respones.get_response(url[times])
            file_size = int(res.headers['Content-Length'])
            with open(f'{file_name}.m4s', 'wb')as f:
                for i in res.iter_content(chunk_size=10240):
                    f.write(i)
            with open(f'{file_name}.m4s', 'r')as f:
                real_size = os.fstat(f.fileno()).st_size
                complete_persent = f'{int(real_size/file_size*100)} %'
                if file_size == real_size:
                    print(f'链接{times} 下载完成')
                    break
                else:
                    print(f'链接{times} 下载失败\n本应下载大小：{file_size}\n实际下载大小：{real_size}\n完成度：{complete_persent}')
                    raise IOError('Data broken')
        except IOError:
            time.sleep(1)
            times = times + 1


def download(name, a_url, v_url, d_path):  # 主程序
    if not os.path.exists(f'{d_path}/{name}.mp4'):
        print(f'下载视频：{name}')
        v_name = f'{d_path}/{name}v'
        a_name = f'{d_path}/{name}a'
        print('下载视频分块')
        chips(v_name, v_url)
        print('下载音频分块')
        chips(a_name, a_url)
        print(f'开始合并视频文件：{name}')
        cmd = f'ffmpeg -i "{v_name}.m4s" -i "{a_name}.m4s" -c:v copy -c:a copy -strict experimental "{d_path}/{name}.mp4" -loglevel quiet'
        subprocess.call(cmd, shell=True)
        os.remove(f'{v_name}.m4s')
        os.remove(f'{a_name}.m4s')
    print(f'{name}--完成')

#test_name = '《獭獭突然想到》第1话如果猫长到十米高'
#test_path = '/root/bilibili/download/cartoon/獭獭突然想到--SP'
#test_v_url = ['https://xy123x139x63x184xy.mcdn.bilivideo.cn:4483/upgcxcode/25/38/215653825/215653825_p1-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1663062341&gen=playurlv2&os=mcdn&oi=453838542&trid=0000154a8957688d42a9b38cc8d357b314a2p&mid=470586328&platform=pc&upsig=d60192fe1964fe3b17c239bdd63b54ff&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1002263&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=24042&logo=A0000001', 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/25/38/215653825/215653825_p1-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1663062341&gen=playurlv2&os=coso1bv&oi=453838542&trid=154a8957688d42a9b38cc8d357b314a2p&mid=470586328&platform=pc&upsig=705c2bd934a2d823b21a8733d827bcef&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=24042&logo=40000000', 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/25/38/215653825/215653825_p1-1-30280.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1663062341&gen=playurlv2&os=cosbv&oi=453838542&trid=154a8957688d42a9b38cc8d357b314a2p&mid=470586328&platform=pc&upsig=dc8d18f789da0a6ea9f0442337f26c58&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=24042&logo=40000000'] 
#test_a_url=['https://xy123x139x63x184xy.mcdn.bilivideo.cn:4483/upgcxcode/25/38/215653825/215653825_sr1-1-100035.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1663062341&gen=playurlv2&os=mcdn&oi=453838542&trid=0000154a8957688d42a9b38cc8d357b314a2p&mid=470586328&platform=pc&upsig=bb8087c72106f89e0844f089b945750f&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&mcdnid=1002263&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=565638&logo=A0000001', 'https://upos-sz-mirrorcoso1.bilivideo.com/upgcxcode/25/38/215653825/215653825_sr1-1-100035.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1663062341&gen=playurlv2&os=coso1bv&oi=453838542&trid=154a8957688d42a9b38cc8d357b314a2p&mid=470586328&platform=pc&upsig=29057311bd21a75179b430d13aa5b09e&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=1,3&agrr=1&bw=565638&logo=40000000', 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/25/38/215653825/215653825_sr1-1-100035.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1663062341&gen=playurlv2&os=cosbv&oi=453838542&trid=154a8957688d42a9b38cc8d357b314a2p&mid=470586328&platform=pc&upsig=b6fec2d9e759133ad4fff79effb141bf&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=2,3&agrr=1&bw=565638&logo=40000000']
#download(test_name, test_a_url, test_v_url, test_path)
