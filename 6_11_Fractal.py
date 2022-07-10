'''
Изобразите фрактал Жюлиа.
'''
from matplotlib import pyplot as plt
import numpy as np


RE_LIMITS = (-2, 2)
IM_LIMITS = (-2, 2)
POINTS = 1000

THRESHOLD = 1e+4
C = 2.1j


im = np.zeros((POINTS, POINTS))
for i, x in enumerate(np.linspace(*RE_LIMITS, num=POINTS)):
    for j, y in enumerate(np.linspace(*IM_LIMITS, num=POINTS)):
        z = x + y * 1j
        for n in range(100):
            z = z ** 3 + C
            if abs(z) > THRESHOLD:
                break
        im[j, i] = n
plt.imshow(im)
plt.show()
