import cv2
import numpy as np
from key_gen import keyGen

filename = raw_input("Please give us the filename: ")
slave = cv2.imread(filename)
num = raw_input("inter a number between 40-80: ").strip()
num = int(num)
 
shape = slave.shape
keyGen(shape, num)
img2  = cv2.imread("Result/key.png")

a = np.ones(shape)
a = np.multiply(num, a)

temp = np.subtract( np.multiply(a , img2), slave)
img = np.floor_divide(temp, np.subtract(img2, a)) 
img1 = np.remainder(temp, np.subtract(img2, a))

cv2.imwrite("Result/part1.png", img)
cv2.imwrite("Result/part2.png", img1)


