# 需要改路径
# .replace(' ', '').replace('&amp;', '').replace('&lt;', '').replace('&#x27;', '').replace('&gt;', '').replace('&quot;', '').replace('&#770;', '').replace('&#771;', '').replace('|', '').replace('*', '').replace('?', '').replace(':', '').replace('/', '').replace('\\', '').replace('\"', '').replace('<', '').replace('>', '')
import json
import os.path

cookies_path = r'UserData/cookies.json'
if os.path.exists(cookies_path):
    f = json.loads(json.dumps(eval(open(cookies_path, 'r', encoding='utf-8').read())))
    cookies = f['cookies']
    if f['cookies'] != {}:
        dedeuserid = cookies['DedeUserID']
        bili_jct = cookies['bili_jct']
