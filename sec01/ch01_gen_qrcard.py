#!/usr/bin/env python
# encoding: utf-8

"""
@description: 出入证

@author: baoqiang
@time: 2020/7/8 3:12 下午
"""
import os
import random
import shutil

import qrcode
from PIL import Image, ImageDraw, ImageFont


def run():
    gen_qr_card()


def gen_qr_card():
    # image obj
    image = Image.new("RGB", (900, 540), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    # font = ImageFont.truetype("msyhl.ttc", size=45)

    # MAC系统选取字体样式font_medium_type = '/System/Library/Fonts/PingFang.ttc'
    # Windows系统选取字体样式font_medium_type = r'C:\Windows\Fonts\msyh.ttc'
    # 设置字体样式text_font = ImageFont.truetype(font_medium_type, fontSize)

    # input message
    # community = input('\n社区: ')
    community = '京怡花园'
    font = ImageFont.truetype("PingFang.ttc", size=80)
    draw.text((50, 40), community, fill='rgb(0,0,0)', font=font)

    idno = 'ID {}'.format(random.randint(1000000, 9999999))
    font = ImageFont.truetype("PingFang.ttc", size=60)
    draw.text((500, 65), idno, fill='rgb(0,0,0)', font=font)

    # input_name = input('\n姓名: ')
    input_name = 'xiaobao'
    name = '姓名：{}'.format(input_name)
    font = ImageFont.truetype("PingFang.ttc", size=45)
    draw.text((50, 220), name, fill='rgb(0,0,0)', font=font)

    # input_gender = input('\n性别: ')
    input_gender = '男'
    gender = '性别：{}'.format(input_gender)
    draw.text((50, 320), gender, fill='rgb(0,0,0)', font=font)

    # input_house = input('\n门牌号: ')
    input_house = '501B4F603'
    house = '门牌号：{}'.format(input_house)
    draw.text((50, 420), house, fill='rgb(0,0,0)', font=font)

    # save image
    image_file = '../data/{}.png'.format(input_name)
    qr_file = '../data/{}.bmp'.format(idno)
    image.save(image_file)

    # save qrcode
    qr_image = qrcode.make('{}:{}'.format(community, input_name))
    qr_image.save(qr_file)

    # paste
    p1 = Image.open(image_file)
    p2 = Image.open(qr_file)

    p1.paste(p2, (520, 180))
    p1.save(image_file)

    # del qrcode
    os.remove(qr_file)

    # log
    print('gen qr_card ok: {}'.format(image_file))


if __name__ == '__main__':
    run()
