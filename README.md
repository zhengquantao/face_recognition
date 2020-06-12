# face_recognition
基于python+django+dlib实现的人脸打卡系统
## 开始之前 
windows用户需要安装 [VS2017](https://blog.csdn.net/fengbingchun/article/details/83990685) 其他VS版本也行

linux用户需要安装c++编译器(网上很多方法自己搜)
## 起源
这个是我的毕业设计~~~
## 安装 
```bash
# code install 
git clone https://github.com/zhengquantao/face_recognition  # (如果你没有git,也可以直接下载这个文件)
cd face_recognition                                         # 进入这个文件
pip install -r requirement.txt                              # 安装依赖
python manage.py runserver 127.0.0.1:8000                   # 执行
```

## 安装问题

windows用户 如果你有安装dlib失败，可能是以下原因

1.没有安装 [vs](https://blog.csdn.net/fengbingchun/article/details/83990685) 或者其他的包

2.没有将 [cmake](https://blog.csdn.net/weixin_41799903/article/details/90267286) 加入到系统环境中

## 注意
登录账号  密码

1. 2016032528  123456 (管理员)
2. 2016032529  123456 (职工)
3. 2016032531  123456 (职工)
4. 2016032518  123456 (职工)
### 效果图
* success
<img src="https://github.com/zhengquantao/face_recognition/tree/master/static/images/success.png" width="100%">
* fail
<img src="https://github.com/zhengquantao/face_recognition/tree/master/static/images/fail.png" width="100%">
* home
<img src="https://github.com/zhengquantao/face_recognition/tree/master/static/images/home.png" width="100%">
* login
<img src="https://github.com/zhengquantao/face_recognition/tree/master/static/images/login.png" width="100%">

### contact me
如果你有问题可以联系下面的email


Gmail: zhengquantao80@gmail.com
Qmail: 1483906080@qq.com