import cv2
import numpy as np
from key_gen import keyGen
from encrypt import encrypt

filename = "test.webm"
num = 10

cap = cv2.VideoCapture(filename)
ret, slave = cap.read()
shape = slave.shape
keyGen(shape, num)
img2 = cv2.imread("Result/key.png")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
fourcc1 = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Result/part1.avi',fourcc, 30.0, (int(shape[1]),int(shape[0])))
out1 = cv2.VideoWriter('Result/part2.avi',fourcc1, 30.0, (int(shape[1]),int(shape[0])))

while(ret):
	img, img1 = encrypt(slave, img2, num)
	out.write(np.uint8(img))
	out1.write(np.uint8(img1))
	ret, slave = cap.read()
	print "Doing.... "

cap.release()
out.release()
out1.release()
