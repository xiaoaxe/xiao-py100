#!/usr/bin/env python
# encoding: utf-8

"""
@description: 图片下载

@author: baoqiang
@time: 2020/7/8 8:37 下午
"""

import requests
import sys
import time


def run():
    download_pic()


# http://t7.baidu.com/it/u=3616242789,1098670747&fm=79&app=86&f=JPEG?w=900&h=1350
def download_pic():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = 'http://t7.baidu.com/it/u=3616242789,1098670747&fm=79'
    filename = '../data/img_{}.png'.format(int(time.time()))
    with open(filename, 'wb') as fw:
        resp = requests.get(url)
        fw.write(resp.content)

    print('download pic ok: {}'.format(filename))


if __name__ == '__main__':
    run()
