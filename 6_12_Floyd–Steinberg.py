'''
Реализуйте алгоритм Флойда-Стейнберга с помощью NumPy.

Старайтесь максимально использовать возможности NumPy.
'''
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img_name = 'C:\\Users\\ivcbibl13\\Downloads\\123.jpg' # Cats picture
img = Image.open(img_name)
img = img.convert('L')

width, height = img.size
new_width = 400
new_height = int(height * new_width / width)
img = img.resize((new_width, new_height), Image.ANTIALIAS)

arr = np.array(img, dtype=float)

print(arr.shape)
print(arr)

threshold = 96
for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        mean = arr[x][y]
        old_pix = mean
        if mean < threshold:
            new_pix = 0
            arr[x][y] = 0
        else:
            new_pix = 255
            arr[x][y] = 255
        error = old_pix - new_pix
        if x < arr.shape[0] - 1 and arr.shape[1] - 1 > y >= 1:
            arr[x][y + 1] += int((7 / 16.0) * error)
            arr[x + 1][y + 1] += int((1 / 16.0) * error)
            arr[x + 1][y] += int((5 / 16.0) * error)
            arr[x + 1][y - 1] += int((3 / 16.0) * error)


plt.imshow(arr, cmap='gist_gray')
plt.show()
