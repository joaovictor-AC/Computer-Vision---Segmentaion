import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('image.png', cv.IMREAD_GRAYSCALE)
# plt.imshow(img, 'gray', vmin=0, vmax=255)
# plt.show()
# plt.hist(img.ravel(), 256, [0, 256])
# plt.show()


# ret2,th2 = cv.threshold(img,84,255,cv.THRESH_TOZERO)
# plt.imshow(th2, 'gray', vmin=0, vmax=255)
# print(np.mean(th2))
# plt.show()

img2 = img
arr = []
images = []

height, width = img.shape
W_size = 2
H_size = 3

for i_h in range(H_size):
    arr_x = []
    
    for i_w in range(W_size):

        x = width / W_size * i_w
        y = height / H_size * i_h
        h = height / H_size
        w = width / W_size

        img = img[int(y): int(y+h), int(x): int(x+w)]
        ret, th = cv.threshold(img, 0, 255, cv.THRESH_TOZERO+cv.THRESH_OTSU)
        images.append(img)
        arr_x.append(th)
        img = img2
        
    arr.append(arr_x)

for i in range(W_size*H_size):
    plt.subplot(1,2,1),plt.imshow(images[i],'gray')
    plt.subplot(1,2,2),plt.hist(images[i].ravel(),256)
    plt.show()
     

arr_y = []

for el in arr:
    horizontal = cv.hconcat(el)
    arr_y.append(horizontal)

img_joined = cv.vconcat(arr_y)
print(img_joined.size)
plt.imshow(img_joined, 'gray', vmin=0, vmax=255)
plt.show()