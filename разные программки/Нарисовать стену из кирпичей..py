# -*- coding: utf-8 -*-

# (цикл for)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

import simple_draw as sd

width = 100
height = 50

y = 0
y_0 = 0
y_1 = 50

for r in range(12):
    if r % 2 == 0:
        x = 0
    else:
        x = width / 2
    y += 50
    start_point = sd.get_point(0, y)
    end_point = sd.get_point(600, y)
    sd.line(start_point=start_point, end_point=end_point, color=sd.COLOR_ORANGE, width=6)
    for row_v in range(7):
        start_point1 = sd.get_point(x, y_0)
        end_point1 = sd.get_point(x, y_1)
        sd.line(start_point=start_point1, end_point=end_point1, color=sd.COLOR_ORANGE, width=6)
        x += width
    y_0 += height
    y_1 += height

sd.pause()
