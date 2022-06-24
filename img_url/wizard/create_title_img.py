#!/usr/bin/env python
# coding=utf-8
import random
from PIL import Image, ImageDraw, ImageFont
import re
import math
from pathlib import Path
import time
import os

font_bg_color = [{
    "font": '#FF7E00',
    "bg": "black",
}, {
    "font": '#04913B',
    "bg": "black",
}, {
    "font": '#FFFF08',
    "bg": "black",
}, {
    "font": '#02ABE9',
    "bg": "black",
}, {
    "font": '#FBCEE5',
    "bg": "black",
}, {
    "font": '#FFCC00',
    "bg": "#373737",
}, {
    "font": '#ffffff',
    "bg": "#373737",
}, {
    "font": '#F14FBA',
    "bg": "black",
}, {
    "font": '#ffffff',
    "bg": "#FF375B",
}, {
    "font": '#ffffff',
    "bg": "#FD7F00",
}, {
    "font": '#FF7E00',
    "bg": "black",
}, {
    "font": '#FAAF00',
    "bg": "#9F1C03",
}, {
    "font": '#FF7E00',
    "bg": "black",
}, {
    "font": '#ffffff',
    "bg": "#C06D77"}]
background_color = ['#FF7E00', '#04913B', '#FFFF08', '#02ABE9', '#FBCEE5', '#FFCC00', '#87CA6D', '#F14FBA', '#FE0000',
                    '#AFFD88', '#FFCC00', '#ffffff', '#ffffff', '#ffffff', '#F5EE1F', '#FAAF00', '#ffffff']


# 调用gbk编码  中文两个字符，英文和英文符号一个字符 避免文字显示不全  奇数字符后加空格
# todo 大写英文字符 == 中文字符
def transform_gbk_coding_len(text=None):
    pattern = "[A-Z]"
    text = re.sub(pattern, lambda x: x.group(0) + "*", text)
    re_rule = re.compile('[\d+|\u0041-\u005a|\u0061-\u007a| !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+')
    inx = 0
    for r in re_rule.finditer(text):
        r_value = r.group()
        if len(r_value) % 2 != 0:
            text = text[0:r.start() + inx] + r_value + ' ' + text[r.end() + inx:]
            inx += 1
    cut_bytes = text.encode('gbk')
    return cut_bytes


# 获取新标题
def get_arrangement_new_title(text=None, word_count=None):
    show_list = [text[i:i + word_count * 2] + "\n".encode('gbk') for i in
                 range(0, len(text), word_count * 2)]
    a_bytes = "".encode('gbk')
    for i in show_list:
        a_bytes += i
    show_text = a_bytes.decode('gbk', errors='ignore')  # 按bytes截取时有小部分无效的字节，传入errors='ignore'忽略错误
    return show_text.replace('*', '')


# 获取最佳排列
def get_best_permutation(img_width, img_height, text=None):
    text_count = int(len(text) / 2)
    max_min = 100
    max_value = []
    for r in range(1, text_count + 2):
        # print("一排个数:", r)
        # print("边长:", math.floor(img_width / r))
        # print("需要多少排:", math.ceil(text_count / r))
        # print("可以多少排:", math.floor(img_height / math.floor(img_width / r)))
        if math.floor(img_height / math.floor(img_width / r)) >= math.ceil(text_count / r):
            if abs(math.floor(img_height / math.floor(img_width / r)) - math.ceil(text_count / r)) == max_min:
                max_value.append((r, math.floor(img_width / r)))
            if abs(math.floor(img_height / math.floor(img_width / r)) - math.ceil(text_count / r)) < max_min:
                max_min = abs(math.floor(img_height / math.floor(img_width / r)) - math.ceil(text_count / r))
                max_value.append((r, math.floor(img_width / r)))
    return max_value


# 生成img
def create_img(xg_img_width, xg_img_height, border, text=None, font_size=None):
    rad_style = random.choice(font_bg_color)
    image = Image.new("RGB", (xg_img_width, xg_img_height), rad_style['bg'])
    draw_table = ImageDraw.Draw(im=image)
    print(f"{str(Path.cwd())}\\myaddons\\img_url\\wizard\\AaXinHuaMoZhuTi-2.ttf")
    print(Path.cwd())

    path_cwd = os.path.dirname(__file__)  # 先找到当前文件 a.py 所在的目录
    # path = os.path.dirname(path)     # 往上倒一层目录,也就是 config.txt 所在的文件夹
    path = os.path.join(path_cwd, 'AaXinHuaMoZhuTi-2.ttf')  # 拼接文件的路径

    # path_cwd = str(Path.cwd()) + "\\myaddons\\img_url\\wizard\\AaXinHuaMoZhuTi-2.ttf"
    # print(path_cwd)
    draw_table.text(xy=(border, border), text=text, fill=rad_style['font'],
                    font=ImageFont.truetype(path,
                                            font_size))
    # image.show()  # 直接显示图片
    img_path = os.path.join(path_cwd, 'lslj.png')  # 拼接文件的路径
    image.save(f"{Path.cwd()}/myaddons/img_url/wizard/lslj.png", 'PNG')  # 保存在当前路径下，格式为PNG
    # image.close()


def run_main(xg_img_width, xg_img_height, title, border=0):
    # xg_img_width = 600
    # xg_img_height = 400
    # border = 20
    img_width = xg_img_width - border * 2
    img_height = xg_img_height - border * 2

    if img_height > img_width:
        img_width, img_height = img_height, img_width
    # title = "Nginx Proxy Manager 域名管理解析神器"
    new_title = transform_gbk_coding_len(text=title)
    max_value_list = get_best_permutation(img_width=img_width, img_height=img_height, text=new_title)
    for value in max_value_list:
        arrangement_title = get_arrangement_new_title(new_title, value[0])
        print(arrangement_title, value)
        create_img(xg_img_width=xg_img_width, xg_img_height=xg_img_height, border=border, text=arrangement_title,
                   font_size=value[1])
        path_cwd = os.path.dirname(__file__)  # 先找到当前文件 a.py 所在的目录
        return os.path.join(path_cwd, 'lslj.png')


# todo 添加边框
if __name__ == '__main__':
    run_main(600, 400, "红糖、阿胶能补血？你被骗了 ——《曾医生让你早知道》", border=20)
    # xg_img_width = 600
    # xg_img_height = 400
    # border = 20
    # img_width = xg_img_width - border * 2
    # img_height = xg_img_height - border * 2
    #
    # if img_height > img_width:
    #     img_width, img_height = img_height, img_width
    # title = "Nginx Proxy Manager 域名管理解析神器"
    # new_title = transform_gbk_coding_len(text=title)
    # max_value_list = get_best_permutation(text=new_title)
    # print("max_value_list", max_value_list)
    # for value in max_value_list:
    #     arrangement_title = get_arrangement_new_title(new_title, value[0])
    #     print(arrangement_title, value)
    #     create_img(arrangement_title, value[1])
