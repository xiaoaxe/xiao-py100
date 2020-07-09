#!/usr/bin/env python
# encoding: utf-8

"""
@description: flask web app

@author: baoqiang
@time: 2020/7/9 12:53 下午
"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "ok"


@app.route("/hello/<name>")
def hello(name):
    """
    http://localhost:8888/hello/xiao?age=18
    """
    age = request.args.get('age')
    # school = request.form['school']
    return 'Got: name={}, age={}'.format(name, age)


def run():
    app.run(host="localhost", port=8888)


if __name__ == '__main__':
    run()
