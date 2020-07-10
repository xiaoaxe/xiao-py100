#!/usr/bin/env python
# encoding: utf-8

"""
@description: 模拟生成一个时钟

@author: baoqiang
@time: 2020/7/10 12:41 下午
"""

from turtle import Turtle
from datetime import *
import turtle

tur = Turtle()


def run():
    draw_clock()


# main
def draw_clock():
    """
    https://blog.csdn.net/i_chaoren/article/details/57474714
    """
    tur._tracer(False)
    init()
    setup_clock(160)
    tur._tracer(True)
    tick()

    turtle.mainloop()


# helper
def skip(step):
    tur.penup()
    tur.forward(step)
    tur.pendown()


def mk_hand(name, length):
    tur.reset()
    skip(-length * 0.1)
    tur.begin_poly()
    skip(length * 1.1)
    tur.end_poly()
    hand_form = tur.get_poly()
    turtle.register_shape(name, hand_form)


def init():
    global sec_hand, min_hand, hur_hand, printer, printer2

    turtle.setup(400, 400, 800, 400)  # 窗体
    turtle.screensize(300, 300, "pink")  # 画布
    turtle.mode('logo')

    mk_hand('sec_hand', 135)
    mk_hand('min_hand', 110)
    mk_hand('hur_hand', 90)

    sec_hand = Turtle()
    sec_hand.shape("sec_hand")
    min_hand = Turtle()
    min_hand.shape("min_hand")
    hur_hand = Turtle()
    hur_hand.shape("hur_hand")

    for hand in sec_hand, min_hand, hur_hand:
        hand.shapesize(1, 1, 3)
        hand.speed(0)

    printer = Turtle()
    printer.hideturtle()
    printer.penup()

    printer2 = Turtle()
    printer2.hideturtle()
    printer2.penup()


def setup_clock(radius):
    tur.reset()
    tur.pensize(7)

    for i in range(60):
        skip(radius)
        if i % 5 == 0:
            tur.forward(20)
            skip(-radius - 20)
        else:
            tur.dot(5)
            skip(-radius)

        tur.right(6)


def week(t):
    # week = ['星期一', '星期二', '星期三', '星期四',
    #         '星期五', '星期六', '星期日', ]
    # return week[t.weekday()]

    week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return '{:02d}:{:02d}:{:02d} {}'.format(t.hour, t.minute, t.second, week[t.weekday()])


def date(t):
    return '{:04d}-{:02d}-{:02d}'.format(t.year, t.month, t.day)


refresh_cnt = 0


def tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second / 60.0
    hour = t.hour + minute / 60.0
    sec_hand.setheading(6 * second)  # 每秒转动6度
    min_hand.setheading(6 * minute)
    hur_hand.setheading(30 * hour) # 每小时转动30度

    # draw
    tur._tracer(False)

    # reset
    printer.clear()
    printer.hideturtle()
    printer.penup()

    printer.forward(65)  # 中心点往上65个像素
    printer.write(week(t), align='center', font=('Courier', 14, 'bold'))

    printer.home()
    tur._tracer(True)

    # draw static img
    global refresh_cnt
    if refresh_cnt == 0 or (t.hour == 0 and t.minute == 0 and t.second < 3):
        tur._tracer(False)

        # reset
        printer2.clear()
        printer2.hideturtle() #隐藏画笔
        printer2.penup()

        printer2.back(65)
        printer2.write(date(t), align='center', font=('Courier', 14, 'bold'))
        printer2.back(50)
        printer2.write('xiaobao', align='center', font=('Courier', 14, 'bold'))
        printer2.home()

        tur._tracer(True)

    # add one
    refresh_cnt += 1

    turtle.ontimer(tick, 1000)  # 每1000ms，调用一次tick


if __name__ == '__main__':
    run()
