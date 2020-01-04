import random
import sys
import turtle

turtle.speed(0)

coord_list = []
coord = open('coord.txt')

# читаем координаты из файла
for line in coord:
    line = line.strip().split(',')
    nums = []
    for n in line:
        nums.append(int(n))
    coord_list.append(nums)


def gotoxy(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_line(from_x, from_y, to_x, to_y):
    gotoxy(from_x, from_y)
    turtle.goto(to_x, to_y)


def draw_head(x, y, r):
    gotoxy(x, y)
    turtle.circle(r)


def erase(x, y):
    gotoxy(x, y)
    turtle.color('white')
    turtle.begin_fill()
    turtle.begin_poly()
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.fd(200)
    turtle.left(90)
    turtle.fd(50)
    turtle.left(90)
    turtle.end_poly()
    turtle.end_fill()


funcs = [draw_line, draw_line, draw_line, draw_line,
         draw_head, draw_line, draw_line, draw_line, draw_line, draw_line]


def draw_gibbet(step, coord):
    turtle.color('blue')
    funcs[step](*coord_list[step])


x = random.randint(1, 100)

answer = turtle.textinput('Играть ?', 'y/n')

if answer == 'n':
    sys.exit()

hints = False
answer = turtle.textinput('Давать подсказки ?', 'y/n')
if answer == 'y':
    hints = True

try_count = 0

while True:
    number = turtle.numinput('Угадайте', 'Число', 0, 0, 100)

    if number == x:
        erase(-150, 100)
        turtle.color('green')
        gotoxy(-150, 200)
        turtle.write('УРА!!! Вы победили!', font=('Arial', 28, 'normal'))
        break

    else:
        turtle.color('red')
        gotoxy(-150, 100)
        turtle.write('Неверно!!!', font=('Arial', 28, 'normal'))
        if hints:
            gotoxy(100, 100 - try_count * 15)
            if number > x:
                turtle.write(str(number) + 'Загаданное число меньше')
            else:
                turtle.write(str(number) + 'Загаданное число больше')

        draw_gibbet(try_count, coord_list)
        try_count += 1
        if try_count == 10:
            gotoxy(-20, 230)
            turtle.write('Вы проиграли!!!', font=('Arial', 44, 'normal'))
