#!/usr/bin/env python
# encoding: utf-8

# TODO description
"""
@description: 

@author: baoqiang
@time: 2020/7/9 1:07 下午
"""
import requests
import socket

# 7日天气
url = 'http://www.tianqiapi.com/api'


def run():
    get_weather()


def get_weather():
    appid, appsecret = read_password()

    params = {
        'version': 'v9',
        'appid': appid,
        'appsecret': appsecret,
        'ip': get_ip(),
    }

    resp = requests.get(url, params=params)

    parse_data(resp.json())


def parse_data(jdata):
    if not jdata:
        return

    msgs = []
    hour_msgs = []
    for idx, item in enumerate(jdata['data']):
        msg = '{}({}): {}'.format(item['date'], item['week'], item['wea'])
        msgs.append(msg)

        if idx == 0:
            for hitem in item['hours']:
                h_msg = '{}:{}'.format(hitem['hours'], hitem['wea'])
                hour_msgs.append(h_msg)

    country, city = jdata['country'], jdata['city']
    beauty_print(country, city, msgs, hour_msgs)

    print('\n\nget weather ok')


# helper
def read_password():
    filename = '../data/tianqiapi_secret.txt'
    with open(filename, 'r') as f:
        data = f.read()
        return data.split(' ')


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    ip = s.getsockname()[0]
    s.close()

    return ip


def beauty_print(country, city, msgs, hmsgs):
    print('{}{}{}'.format('*' * 12, '{}: {}'.format(country, city), '*' * 12))
    print('\n'.join(msgs))
    # print('*' * 30)

    print('{}分时预报{}'.format('*' * 13, '*' * 13))
    for idx, msg in enumerate(hmsgs, start=1):
        msg = '[{}]'.format(msg)
        if idx % 3 == 0:
            print(msg)
        else:
            print(msg, end='\t')


if __name__ == '__main__':
    run()
