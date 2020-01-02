# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (800, 600)

# Реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20


snow = []  # снег с координатами, длиной, скоростью падения, ветром

for n in range(N):
    x = random.randrange(10, 501)
    y = random.randrange(500, 601)
    dlina = random.randrange(10, 101)
    skor = random.random()
    veter = random.randrange(3, 8)
    snow.append([x, y, dlina, skor, veter])

while True:
    sd.start_drawing()

    for item in snow:
        point = sd.get_point(item[0], item[1])
        sd.snowflake(center=point, length=item[2], color=sd.background_color)
        item[1] -= 10 * item[3]

        item[0] = item[0] + item[4] * random.randint(-1, 1)
        point2 = sd.get_point(item[0], item[1])

        if item[1] < 50:
            item[1] = 600
            item[0] = random.randrange(500)
        sd.snowflake(center=point2, length=item[2], color=sd.COLOR_WHITE)
    if sd.user_want_exit():
        break

    sd.finish_drawing()
    sd.sleep(0.1)

sd.pause()

