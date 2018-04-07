import cv2
import numpy as np

img = cv2.imread("Result/part1.png")
img1 = cv2.imread("Result/part2.png")
img2 = cv2.imread("Result/key.png")
shape = img.shape

num = raw_input("inter the number you typed at the time of encryption: ").strip()
num = int(num)

a = np.ones(shape)
a = np.multiply(num, a)

img3 = np.subtract(np.multiply(a, img2) , np.add(np.multiply(np.subtract(img2, a) , img)  , img1))

cv2.imwrite("Result/result.png", img3)


