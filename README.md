# AppEcology
## 项目介绍
将一个个好玩，有趣，实用的功能做成模型，在网站上直接使用。形成一个工具箱类型的网站。
## 技术栈

| 技术栈        | 描述        | 官网                  |
|------------|-----------|---------------------|
| odoo       | python web框架 用来部署模块 | https://odoo.com/   |
| python     | 开发大多使用python语言 | https://python.org/ |
| javascript | 少部分使用     |  |


## 已有功能
1. 运动刷步数（微信，支付宝）：可通过接口调用
2. 图床
3. 每日更新面板
4. 自动化（简陋版）

## api接口文档
[api接口文档](https://www.apifox.cn/apidoc/shared-5f9cf208-339e-4a35-8de1-386f1077ae9a)

## 启动部署
运用docker-compose进行部署
1.[安装docker](https://www.runoob.com/docker/ubuntu-docker-install.html)  
2.[安装docker-compose](https://www.runoob.com/docker/docker-compose.html)  
3.mkdir AppEcology
4.cd AppEcology
5.git clone https://github.com/yxj1028530975/AppEcology
6.cd AppEcology/docker_compose
7.docker-compose up -d

### 环境准备

## TODO
1.慢慢来。。。


## 项目预览

在线预览地址: [账号：demo 密码：demo](http://124.221.153.111:8069/)
在线预览地址: [管理员账号：还需要调试功能](http://124.221.153.111:8069/)
功能测试完后部署到线上

| ![登录界面](http://124.221.153.111:8069//web/content/505?access_token=9d27ba47-5292-4280-8868-39f8d6aabcf8) | ![每日更新面板](http://124.221.153.111:8069//web/content/510?access_token=50e09ef0-f526-400d-a01e-8d70e43a4bc9) |
|-----------------------------------------------------------|--------------------------------------------------------|
| ![修改步数模块](http://124.221.153.111:8069//web/content/507?access_token=6fe2b79c-23d8-4ba3-9c0b-132bcea1492d)    | ![自动化模块](http://124.221.153.111:8069//web/content/512?access_token=d26e244e-175c-4621-991b-d6c738140773)  |
| ![图床模块](http://124.221.153.111:8069//web/content/511?access_token=874f33ec-f964-41a0-baa5-d71b4e31bb1f)     | ![模块管理](https://www.youlai.tech/files/blog/stock.png)  |
待更新....



[安装odoo15](https://github.com/odoo/odoo)  
替换模块 替换 myaddons 有空完善

## 更新日志
2022-6-27
1.修复安装依赖bug

2022-6-27
1.更新了docker_compose的使用
使用方式:git clone https://github.com/yxj1028530975/AppEcology

cd AppEcology/docker_compose

docker-compose up -d

即可启动项目

映射端口:8369

开放服务器端口8369 

访问地址:http://公网ip:8369 即可启动项目

2022-6-24
1.图床上传
2.完善复制链接功能
3.增加图床分类
4.增加图床api接口
5.增加图床token权限

2022-6-21 
1.增加定时任务配置
![](http://124.221.153.111:8069//web/content/515?access_token=e4c4c93d-5d48-46d7-a1b5-d31832af614f)

2022-6-18 
1.优化用户权限，分为用户和管理员
![](http://124.221.153.111:8069//web/content/513?access_token=0d76d775-acb5-4a45-9c4b-34eafc1e3039)
2.增加接口修改步数   例：http://124.221.153.111:8069/api/update?user=user&password=password&update_steps=update_steps 防止接口滥用，需要先在平台绑定账号

![](http://124.221.153.111:8069//web/content/514?access_token=2de99a31-609a-4444-92f1-5c5bf294c7f2)
