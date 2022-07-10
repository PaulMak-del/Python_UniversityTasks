'''
Реализуйте модель сегрегации Шеллинга в Matplotlib. На двумерной сетке находятся агенты двух групп. На каждой клетке может находиться не более 1 агента. 
Агент «счастлив», если, как минимум, заданный количество ближайших соседей относится к его группе. В противном случае агент переезжает на иное, свободное место.

Ввести следующие параметры: размер популяции, размеры сетки, процентное соотношение агентов двух групп, пороговое значение «толерантности», 
количество шагов моделирования.

Реализовать отображение агентов в виде квадратов двух цветов на целочисленной сетке.
Случайно разместить агентов, учитывая запрет на совпадение координат.
Реализовать функцию distance на основе метрики манхэттенского расстояния.
Реализовать функцию is_happy.
Изобразить график исходного расположения агентов и график расположения спустя N шагов моделирования.
Изобразить график изменения состояния «настроения» агентов.
(повышенной сложности) Реализовать анимацию шагов моделирования.
'''
from matplotlib import pyplot as plt
from random import random
import time


# 0 - Red
# 1 - White
# 2 - Blue
def init(field_in):
    red_amount = RATIO * 0.01 * POPULATION_SIZE
    blue_amount = (1 - RATIO * 0.01) * POPULATION_SIZE

    while red_amount + blue_amount > 0:
        if red_amount > 0:
            x = int(random() * FIELD_SIDE)
            y = int(random() * FIELD_SIDE)
            while field_in[x][y] != 1:
                x = int(random() * FIELD_SIDE)
                y = int(random() * FIELD_SIDE)
            field_in[x][y] = 0
            red_amount -= 1
        if blue_amount > 0:
            x = int(random() * FIELD_SIDE)
            y = int(random() * FIELD_SIDE)
            while field_in[x][y] != 1:
                x = int(random() * FIELD_SIDE)
                y = int(random() * FIELD_SIDE)
            field_in[x][y] = 2
            blue_amount -= 1


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def is_happy(field_in, x, y):
    if field_in[x][y] == 1:
        return None
    neighbor_info = [999] * NEAR_NEIGHBOR_AMOUNT
    for i in range(NEAR_NEIGHBOR_AMOUNT):
        neighbor_info[i] = [999] * 2

    for i in range(FIELD_SIDE):
        for j in range(FIELD_SIDE):
            if field_in[i][j] != 1:
                dist = distance(i, j, x, y)
                for k in range(NEAR_NEIGHBOR_AMOUNT):
                    if neighbor_info[k][0] > dist and dist != 0:
                        neighbor_info[k][0] = dist
                        neighbor_info[k][1] = field_in[i][j]
                        break

    red_neighbor = 0
    blue_neighbor = 0
    for i in range(NEAR_NEIGHBOR_AMOUNT):
        if neighbor_info[i][1] == 0:
            red_neighbor += 1
        if neighbor_info[i][1] == 2:
            blue_neighbor += 1

    if field_in[x][y] == 0:
        if blue_neighbor <= TOLERANCE:
            return True
        else:
            return False
    else:
        if red_neighbor <= TOLERANCE:
            return True
        else:
            return False


def update():
    switch_position_check = [False] * FIELD_SIDE * FIELD_SIDE
    for x in range(FIELD_SIDE):
        for y in range(FIELD_SIDE):
            if not switch_position_check[x * FIELD_SIDE + y]:
                if field[x][y] != 1 and not is_happy(field, x, y):
                    temp_x = int(random() * FIELD_SIDE)
                    temp_y = int(random() * FIELD_SIDE)
                    while field[temp_x][temp_y] != 1:
                        temp_x = int(random() * FIELD_SIDE)
                        temp_y = int(random() * FIELD_SIDE)
                    color = field[x][y]
                    field[x][y] = 1
                    field[temp_x][temp_y] = color
                    switch_position_check[x * FIELD_SIDE + y] = True
                    switch_position_check[temp_x * FIELD_SIDE + y] = True


def get_happy_amount(field_in):
    count = 0
    for x in range(FIELD_SIDE):
        for y in range(FIELD_SIDE):
            if is_happy(field_in, x, y):
                count += 1
    return count


# Initializing
POPULATION_SIZE = 300
FIELD_SIDE = 20
RATIO = 50
TOLERANCE = 3
NEAR_NEIGHBOR_AMOUNT = 8
MODELING_STEPS_AMOUNT = 20
assert FIELD_SIDE * FIELD_SIDE > POPULATION_SIZE

field = [1] * FIELD_SIDE
for i in range(FIELD_SIDE):
    field[i] = [1] * FIELD_SIDE

# --------PROGRAM---------
init(field)
happy_array = [-1] * (MODELING_STEPS_AMOUNT + 1)
happy_array[0] = get_happy_amount(field)
steps = 0
plt.ion()

# Main loop
while steps < MODELING_STEPS_AMOUNT:
    steps += 1
    plt.clf()
    plt.imshow(field, cmap='RdYlBu')
    plt.draw()
    plt.gcf().canvas.flush_events()
    time.sleep(0.2)
    update()
    happy_array[steps] = get_happy_amount(field)

plt.ioff()
plt.show()

plt.bar([i for i in range(MODELING_STEPS_AMOUNT + 1)], happy_array)
plt.show()
