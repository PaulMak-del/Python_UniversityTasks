'''
Скачайте игру DandyBot. Код для своего игрока записывается в файле user_bot.py. Игра запускается с помощью main.py.

Вот простой пример содержимого user_bot.py:

def script(check, x, y):
     return 'right'
Игровая логика записывается исключительно в теле функции script. В нашем случае игрок будет постоянно двигаться вправо.

Полный список действий, которые можно возвращать из функции script, задающей "интеллект" игрока:

'up'. Двигаться вверх на клетку.
'down'. Двигаться вниз на клетку.
'left'. Двигаться влево на клетку.
'right'. Двигаться вправо на клетку.
'pass'. Ничего не делать.
'take'. Взять золото.
Для изучения среды есть функция check:

check('player', x, y). True, если какой-то игрок в позиции (x, y).
check('gold', x , y). Если золото в позиции (x, y), то вернуть его количество, иначе вернуть 0.
check('wall', x, y). True, если стена в позиции (x, y).
check('level'). Вернуть номер текущего уровня.
Ваша задача — пройти 4 уровня. Дополнительно устанавливаемыми библиотеками и глобальными данными пользоваться нельзя.
'''

def script(check, x, y):
    if check("gold", x, y):
        return "take"
    field = []
    width = 30
    height = 30

    nearest_distance = 999
    nearest_x = 0
    nearest_y = 0
    for i in range(height):
        field.append([0] * width)
    field[y][x] = 1

    # ---Mark cells---#
    for x_in in range(width):
        for y_in in range(height):
            if check("gold", x_in, y_in) > 0:
                field[y_in][x_in] = -7
                if nearest_distance > (x_in - x) ** 2 + (y_in - y) ** 2:
                    nearest_x = x_in
                    nearest_y = y_in
                    nearest_distance = (x_in - x) ** 2 + (y_in - y) ** 2
            elif check("wall", x_in, y_in) > 0:
                field[y_in][x_in] = -9

    coin_is_not_find = True
    while coin_is_not_find:
        if field[nearest_y][nearest_x + 1] > 0 or field[nearest_y][nearest_x - 1] > 0 or field[nearest_y + 1][nearest_x] > 0 or field[nearest_y - 1][nearest_x] > 0:
            coin_is_not_find = False
        for x_in in range(width):
            for y_in in range(height):
                if field[y_in][x_in] > 0:
                    if x_in < width - 1:
                        if field[y_in][x_in + 1] == 0:
                            field[y_in][x_in + 1] = field[y_in][x_in] + 1
                    if x_in > 0:
                        if field[y_in][x_in - 1] == 0:
                            field[y_in][x_in - 1] = field[y_in][x_in] + 1
                    if y_in < height - 1:
                        if field[y_in + 1][x_in] == 0:
                            field[y_in + 1][x_in] = field[y_in][x_in] + 1
                    if y > 0:
                        if field[y_in - 1][x_in] == 0:
                            field[y_in - 1][x_in] = field[y_in][x_in] + 1

    # ---Mark cells---#

    # ---Find the path---#
    current_x = nearest_x
    current_y = nearest_y

    if check("gold", x + 1, y) > 0:
        return "right"
    if check("gold", x - 1, y) > 0:
        return "left"
    if check("gold", x, y + 1) > 0:
        return "down"
    if check("gold", x, y - 1) > 0:
        return "up"

    count = 999
    while count > 2:
        if 0 < field[current_y][current_x + 1] < count and current_x < width - 1:
            count = field[current_y][current_x + 1]
            if count != 1:
                current_x = current_x + 1
        elif 0 < field[current_y][current_x - 1] < count and current_x > 0:
            count = field[current_y][current_x - 1]
            if count != 1:
                current_x = current_x - 1
        elif 0 < field[current_y + 1][current_x] < count and current_y < height - 1:
            count = field[current_y + 1][current_x]
            if count != 1:
                current_y = current_y + 1
        elif 0 < field[current_y - 1][current_x] < count and current_y > 0:
            count = field[current_y - 1][current_x]
            if count != 1:
                current_y = current_y - 1
    # ---Find the path---#

    # ---Do the move---#
    if x < current_x:
        return "right"
    if x > current_x:
        return "left"
    if y < current_y:
        return "down"
    if y > current_y:
        return "up"

    # ---Do the move---#

    print('Something wrong')
    return "pass"
