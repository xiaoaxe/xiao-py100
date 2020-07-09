#!/usr/bin/env python
# encoding: utf-8

"""
@description: ocr识别

@author: baoqiang
@time: 2020/7/9 8:35 下午
"""

from PIL import Image
import requests
import pytesseract as pt
import os

os.environ['TESSDATA_PREFIX'] = '/usr/local/Cellar/tesseract/4.1.1/share/tessdata'


def run():
    run_ocr()


def run_ocr():
    """
    语言包下载：https://github.com/tesseract-ocr/tessdata
    本地路径：/usr/local/Cellar/tesseract/4.1.1/share/tessdata
    """
    url = 'https://china-testing.github.io/images/python_lib_ocr_en.png'
    img = Image.open(requests.get(url, stream=True).raw)
    text = pt.image_to_string(img)
    print('english: \n{}'.format(text))

    url = 'https://china-testing.github.io/images/python_lib_ocr.PNG'
    img = Image.open(requests.get(url, stream=True).raw)
    text = pt.image_to_string(img, lang='chi_sim')
    print('中文: \n{}'.format(text))

    filename = '../data/tesseract_image.png'
    img = Image.open(filename)
    text = pt.image_to_string(img, lang='chi_sim')
    print('文件中文: \n{}'.format(text))


if __name__ == '__main__':
    run()
