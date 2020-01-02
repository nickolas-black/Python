# -*- coding: utf-8 -*-

import simple_draw as sd



# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#


def figura(nach, ugol, dlina, storana):
    i = int(360 / storana)
    for ug in range(0, 361, i):
        v = sd.get_vector(start_point=nach, angle=ugol + ug, length=dlina, width=3)
        v.draw(color=sd.COLOR_DARK_GREEN)
        nach = v.end_point


def treugol(nach, ugol, dlina):
    storana = 3
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


def kvadrat(nach, ugol, dlina):
    storana = 4
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


def pyti(nach, ugol, dlina):
    storana = 5
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


def shesty(nach, ugol, dlina):
    storana = 6
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


tre = sd.get_point(70, 400)
kvad = sd.get_point(300, 300)
pytiug = sd.get_point(100, 100)
shetiug = sd.get_point(500, 400)

treugol(tre, 50, 200)
kvadrat(kvad, 25, 150)
pyti(pytiug, 35, 100)
shesty(shetiug, 60, 50)


sd.pause()
