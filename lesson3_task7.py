from matplotlib import pyplot as plt
from random import random


def rand_smt():
    points = [round(random()) for i in range((mob_size // 2 + 1) * mob_size)]  # 15 for mob_size = 5

    image1 = [[points[0], points[5], points[10], points[5], points[0]],
             [points[1], points[6], points[11], points[6], points[1]],
             [points[2], points[7], points[12], points[7], points[2]],
             [points[3], points[8], points[13], points[8], points[3]],
             [points[4], points[9], points[14], points[9], points[4]]]

    image2 = [[points[0], points[1], points[2], points[3], points[4]],
             [points[5], points[6], points[7], points[8], points[9]],
             [points[10], points[11], points[12], points[13], points[14]],
             [points[5], points[6], points[7], points[8], points[9]],
             [points[0], points[1], points[2], points[3], points[4]]]

    image3 = [[points[0], points[1], points[2], points[3], points[4]],
             [points[1], points[5], points[6], points[7], points[8]],
             [points[2], points[6], points[9], points[10], points[11]],
             [points[3], points[7], points[10], points[12], points[13]],
             [points[4], points[8], points[11], points[13], points[14]]]

    return image3


array_size = 62
mob_size = 5
array = [0] * array_size
for i in range(array_size):
    array[i] = [0] * array_size

i, j = 0, 0
while array_size - i > mob_size:
    while array_size - j > mob_size:
        image = rand_smt()

        for k in range(mob_size):
            for g in range(mob_size):
                array[i + k][j + g] = image[k][g]
        j += mob_size + 2
    j = 0
    i += mob_size + 2


plt.imshow(array, cmap="Greys")
plt.show()
