# Пример решения Судоко с помощью backtraсk
# доска Судоку заполняется произвольно или так как у Вас есть в доске Судоку.
# для примера заполнил так как показано внизу


board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
# количество подстановок

tries = 0


# функция вывод доски Судоку

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - -')
        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print('| ', end='')
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end='')


# поиск ячеки которая пустая (которая равна 0 )

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                # строка, столбец
                return (i, j)
    return None


# функция перебирает все возможные значения
# и подставляет в пустую ячейку значения
# и проверять верно ли подставила

def valid(bo, num, pos):
    # Проверка строки
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Проверка столбца
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Проверка квадрата
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(bo):
    global tries
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            tries += 1
            if solve(bo):
                return True

            bo[row][col] = 0
    return False


print('________________' * 2)
print('Первоначальная доска Судоку')
print('________________' * 2)
print_board(board)
solve(board)
print('________________' * 2)
print('Результат правильно заполненной доски Судоку')
print('________________' * 2)
print_board(board)
print(f'Решено за {tries} подстановок')
