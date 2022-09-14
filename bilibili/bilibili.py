import urllib.parse
from gevent import monkey
from urllib.parse import quote
# 研究队列来下载
import json
import os
import qrcode

from flask import Flask, request, render_template, send_file, jsonify, redirect
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler


monkey.patch_all()
import User_info
import requests
import b_v_class
import b_v_bvideo
import b_v_drama
import b_v_upvideo
import checkcookies
import download_info
import get_cookies

header = {'origin': 'https://www.bilibili.com', 'referer': 'https://www.bilibili.com',
          'user-agent': 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}

app = Flask(import_name=__name__)
app.config['JSON_AS_ASCII'] = False
app.config.update(DEBUG=True)
print('启动完成')
base_path = os.getcwd().replace('\\', '/')


def get_qr():
    url = 'http://passport.bilibili.com/qrcode/getLoginUrl'
    res = requests.get(url=url, headers=header).json()['data']
    res = str(res).replace('\'', '\"')
    with open('tmp/get_qr.json', 'w') as f:
        f.write(res)
        f.close()


@app.route('/', methods=["GET", "POST"])
def index():
    res = json.loads(checkcookies.check_cookie())
    res = res['code']
    if res == 0:
        user_info = User_info.yourinfo()
        user_info = json.loads(user_info)
        print(user_info)
        return render_template('home.html', info=user_info)
    else:
        get_qr()
        with open('tmp/get_qr.json', 'r') as f:
            res = json.loads(f.read())
        f.close()
        qrurl = '/qr?url=' + quote(str(res['url']))
        return render_template('index.html', qrurl=qrurl)


@app.route('/qr', methods=["GET"])
def qr():
    b_url = request.values.get('url')
    qrcode.make(b_url).save('image.png')
    return send_file(f'image.png')


@app.route('/login', methods=["GET"])
def login():
    res = get_cookies.get()
    if res == 'Success':
        return render_template('home.html')


@app.route('/v/<vv_type>', methods=["GET", "POST"])
def v_type(vv_type):
    os.chdir(base_path)
    if request.method == "POST":
        url = request.form.get('url')
        print(url)
        if vv_type == "bvideo":
            res = b_v_bvideo.bviedio(url)
            keep_res = json.dumps(eval(res), ensure_ascii=False)
            res = json.loads(keep_res)
            return jsonify(res)
            # return render_template('bvideo.html', data=res)
        elif vv_type == "upvideo":
            v_list = b_v_upvideo.upvideo(url)
            res = json.loads(v_list)
            return jsonify(res)
        elif vv_type == "class":
            class_id = request.get_data()
            print(class_id)
            res = json.loads(class_id)
            b_v_class.class_info(res['id'])
            # return jsonify(res)
            return render_template('upvideo.html', data=res)
        elif vv_type == "cartoon":
            data = request.get_data()
            data = json.loads(data)
            b_v_drama.seasons_info(data)
            return jsonify(data)
        elif vv_type == "drama":
            data = request.get_data()
            data = json.loads(data)
            b_v_drama.seasons_info(data)
            return jsonify(data)
    else:
        if vv_type == 'bvideo':
            return render_template('bvideo.html', data={})
        elif vv_type == 'upvideo':
            return render_template('upvideo.html', data={})
        elif vv_type == 'class':
            if not request.args.get('id'):
                res = b_v_class.class_list()
                res = json.loads(res)
                return jsonify(res)
            else:
                class_id = request.args.get('id')
                res = b_v_class.class_info(class_id)
                return jsonify(res)

        elif vv_type == 'cartoon':
            res = b_v_drama.series_list(1)
            res = json.loads(res)
            return jsonify(res)

        elif vv_type == 'drama':
            res = b_v_drama.series_list(2)
            res = json.loads(res)
            return jsonify(res)


@app.route('/auto/<v_type>', methods=["GET", "POST"])
def auto(v_type):
    if request.method == "POST":
        if v_type == 'class':
            class_list = json.loads(b_v_class.class_list())
            for i in class_list:
                b_v_class.class_info(i['id'])
                titel = i['title']
                print(f'自动化class任务:{titel} 完成')
        elif v_type == 'cartoon':
            cartoon_list = json.loads(b_v_drama.series_list(1)
)
            for i in cartoon_list:
                b_v_drama.seasons_info(i)
                titel = i['Name']
                print(f'自动化class任务:{titel} 完成')
        elif v_type == 'drama':
            drama_list = json.loads(b_v_drama.series_list(2)
)
            for i in drama_list:
                b_v_drama.seasons_info(i)
                titel = i['Name']
                print(f'自动化class任务:{titel} 完成')
        else:
            return 404
        return jsonify({"code": 0, "msg": "完成", "data": v_type})
    else:
        return jsonify({"code": -1, "msg": "无效请求", "data": []})


@app.route('/download', methods=["GET", "POST"])
def obj_download():
    if request.method == "POST":
        # data = str(request.get_data()).replace('null', '\"null\"').replace('true', '\"true\"')
        url = request.get_data()
        if url:
            data = json.loads(url)
            url = data['url']
            num = data['num']
            print(f'本次请求的投稿视频url:{url}')
            if url[:8] == 'https://':
                print('url合法')
            else:
                url = urllib.parse.unquote(url)
            print(url)
            res = b_v_bvideo.bviedio(url)
            data = res
            data = json.loads(json.dumps(eval(data)))
            download_info.data_download(data, num)
            return {"code": 0, "msg": "下载完成"}, 200
        else:
            return {"code": -1, "msg": "false"}, 403
    else:
        return {"code": -1, "msg": "hahaha~~~", "data": []}


if __name__ == '__main__':
#     app.run(debug=True, port=9876, host='0.0.0.0')
    http_server = WSGIServer(('0.0.0.0', 5050), app, handler_class=WebSocketHandler)
    http_server.serve_forever()
