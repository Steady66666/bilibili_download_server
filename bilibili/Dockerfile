FROM python:3.10
WORKDIR /bilibili/

#COPY requirements.txt ./
#RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . .
RUN sed -i "s@http://.*archive.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
RUN sed -i "s@http://.*security.ubuntu.com@https://mirrors.tuna.tsinghua.edu.cn@g" /etc/apt/sources.list
#7更新源
RUN pip install asgiref==3.5.2
RUN pip install blinker==1.5
RUN pip install certifi==2022.6.15
RUN pip install cffi==1.15.1
RUN pip install charset-normalizer==2.1.1
RUN pip install click==8.1.3
RUN pip install colorama==0.4.5
RUN pip install Django==4.1
RUN pip install Flask==2.2.2
RUN pip install gevent==21.12.0
RUN pip install gevent-websocket==0.10.1
RUN pip install greenlet==1.1.3
RUN pip install idna==3.3
RUN pip install image==1.5.33
RUN pip install itsdangerous==2.1.2
RUN pip install Jinja2==3.1.2
RUN pip install MarkupSafe==2.1.1
RUN pip install Pillow==9.2.0
RUN pip install pycparser==2.21
RUN pip install qrcode==7.3.1
RUN pip install requests==2.28.1
RUN pip install six==1.16.0
RUN pip install sqlparse==0.4.2
RUN pip install tzdata==2022.2
RUN pip install urllib3==1.26.12
RUN pip install Werkzeug==2.2.2
RUN pip install zope.event==4.5.0
RUN pip install zope.interface==5.4.0


RUN apt-get update
RUN apt-get -y install yasm ffmpeg


ENTRYPOINT ["python","bilibili.py"]
EXPOSE 5050