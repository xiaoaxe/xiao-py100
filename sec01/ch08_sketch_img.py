#!/usr/bin/env python
# encoding: utf-8

"""
@description: 图片转素描画

@author: baoqiang
@time: 2020/7/10 7:41 下午
"""

import cv2

def run():
    to_sketch()


def to_sketch():
    """
    https://www.bilibili.com/video/BV1dJ411b71o
    """
    src_filename = '../data/img_1594269998.png'
    dst_filename = '../data/img_1594269998_sketch.png'

    img_rgb = cv2.imread(src_filename)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    img_blue = cv2.GaussianBlur(img_gray, ksize=(21, 21), sigmaX=0, sigmaY=0)
    img_blend = cv2.divide(img_gray, img_blue, scale=255)  # 除法运算，改变的是每个像素的颜色深度
    cv2.imwrite(dst_filename, img_blend)


if __name__ == '__main__':
    run()
