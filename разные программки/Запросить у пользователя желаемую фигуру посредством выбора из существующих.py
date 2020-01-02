# -*- coding: utf-8 -*-

import simple_draw as sd


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана


def figura(nach, ugol, dlina, storana):
    i = int(360 / storana)
    for ug in range(0, 361, i):
        v = sd.get_vector(start_point=nach, angle=ugol + ug, length=dlina, width=3)
        v.draw(color=sd.COLOR_DARK_GREEN)
        nach = v.end_point


def treugol():
    storana = 3
    nach = sd.get_point(200, 200)
    dlina = 100
    ugol = 30
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


def kvadrat():
    storana = 4
    nach = sd.get_point(200, 200)
    dlina = 100
    ugol = 30
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


def pyti():
    nach = sd.get_point(200, 200)
    storana = 5
    dlina = 100
    ugol = 30
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


def shesty():
    nach = sd.get_point(200, 200)
    storana = 6
    dlina = 100
    ugol = 30
    return figura(nach=nach, ugol=ugol, dlina=dlina, storana=storana)


def print_them_all_v(**kwargs):
    print('Возможные фигуры:')
    for key, value in kwargs.items():
        print(key, ':', value)


def find_element(tree, elem):
    func = {'0': treugol, '1': kvadrat, '2': pyti, '3': shesty}
    if elem in tree:
        func[elem]()
        return


numer_figury = {
    '0': 'треугольник',
    '1': 'квадрат',
    '2': 'пятиугольник',
    '3': 'шестиугольник'
}

print_them_all_v(**numer_figury)

while True:
    n = input('Введите желаемую фигуру от 0 до 3: ')
    if n in numer_figury:
        find_element(numer_figury, n)
        break
    else:
        print('Вы ввели некорректную фигуры!!!')

sd.pause()

