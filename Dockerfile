FROM python:3.6.3

# 设置工作目录
RUN mkdir -p /home/xiao/flask-docker/app
WORKDIR /home/xiao/flask-docker/app

#添加依赖，利用docker的缓存
ADD ./requirements.txt /home/xiao/flask-docker/app/requirements.txt

#安装依赖
RUN pip install -r requirements.txt

#添加应用
ADD . /home/xiao/flask-docker/app

#运行服务
CMD python manage.py runserver -h 0.0.0.0
