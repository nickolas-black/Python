# -*- coding: utf-8 -*-


import simple_draw
import turtle
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
sm = turtle.Pen()
sm.speed(0)
sm.hideturtle()

window = turtle.Screen()
window.bgcolor('black')


def draw_smiley(dl, vs):
    sm.penup()
    sm.setpos(dl, vs)
    sm.pendown()
    # голова
    sm.pencolor('yellow')
    sm.fillcolor('yellow')
    sm.begin_fill()
    sm.circle(50)
    sm.end_fill()
    # левый глаз
    sm.setpos(dl - 15, vs + 60)
    sm.fillcolor('blue')
    sm.begin_fill()
    sm.circle(10)
    sm.end_fill()
    # правый глаз
    sm.setpos(dl + 15, vs + 60)
    sm.fillcolor('blue')
    sm.begin_fill()
    sm.circle(10)
    sm.end_fill()
    # рот
    sm.setpos(dl - 25, vs + 40)
    sm.pencolor('black')
    sm.width(10)
    sm.goto(dl - 10, vs + 20)
    sm.goto(dl + 10, vs + 20)
    sm.goto(dl + 25, vs + 40)
    sm.width(1)


x_min = -window.window_width() // 2
x_max = window.window_width() // 2
y_min = -window.window_height() // 2
y_max = window.window_height() // 2
for n in range(10):
    x = random.randrange(x_min, x_max)
    y = random.randrange(y_min, y_max)
    draw_smiley(x, y)

simple_draw.pause()
