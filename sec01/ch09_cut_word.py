#!/usr/bin/env python
# encoding: utf-8

"""
@description: 结巴分词

@author: baoqiang
@time: 2020/7/10 8:40 下午
"""

import jieba
from collections import Counter


def run():
    cut_word()


stop_words = set()


def load_stop_words():
    filename = '../data/stop_words.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            stop_words.add(line.strip())


def cut_word():
    load_stop_words()

    filename = '../data/ent_news.txt'
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()

    seg_list = jieba.cut(data)
    # for word in seg_list:
    #     print(word)

    word_list = []
    for word in seg_list:
        if word not in stop_words:
            word_list.append(word)

    counter = Counter(word_list)
    for word, num in counter.most_common(10):
        print(word, num)


if __name__ == '__main__':
    run()
