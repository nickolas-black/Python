# -*- coding: utf-8 -*-

import simple_draw as sd
import random

sd.resolution = (600, 600)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)
#
# def branch(point, angle, length, delta):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * .75
#     branch(point=next_point, angle=next_angle, length=next_length, delta=delta)
#
# for delta in range(0, 51, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)
# for delta in range(-50, 1, 10):
#     branch(point=point_0, angle=90, length=150, delta=delta)

# дерево

def branch(nach, angle, length, width):
    if length < 5:
        return
    v = sd.get_vector(start_point=nach, angle=angle, length=length, width=width)
    v.draw(color=sd.COLOR_DARK_GREEN)
    u = random.randint(25, 55)
    branch(nach=v.end_point, angle=angle - 30, length=length * random.random(), width=width)
    branch(nach=v.end_point, angle=angle + u, length=length * 0.75, width=width)
    branch(nach=v.end_point, angle=angle + 30, length=length * random.random(), width=width)


point_0 = sd.get_point(300, 30)

branch(point_0, 90, 100, 3)

sd.pause()
