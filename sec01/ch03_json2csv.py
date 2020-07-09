#!/usr/bin/env python
# encoding: utf-8

"""
@description: pandas处理文本

@author: baoqiang
@time: 2020/7/8 8:45 下午
"""

import pandas as pd


def run():
    json_to_csv()


def json_to_csv():
    """
    {"id": 1,"name":"xiao","age":16}
    {"id": 2,"name":"yu","age":14}
    {"id": 3,"name":"pig","age":22}
    """
    input_file = '../data/pd_sample.json'
    output_file = '../data/pd_sample.csv'

    # read
    df = read_json(input_file)
    df.set_index('id', inplace=True)

    # filter
    df = df[df['age'] < 18]

    # and filter
    # df = df[(df['price'] >= 300) & (df['price'] <= 450)]
    # str not contains filter
    # df = df[(~df['structure'].str.contains('房间'))]

    # save
    print(df.head(5))
    # df.to_csv(output_file, index=False)
    df.to_csv(output_file)


def read_json(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        datas = (line.strip() for line in f)
        datas = '[{}]'.format(','.join(datas))

    return pd.read_json(datas)


if __name__ == '__main__':
    run()
