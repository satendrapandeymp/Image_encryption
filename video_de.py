import cv2
import numpy as np
from decrypt import decrypt

filename = 'Result/part1.avi'
filename1 = 'Result/part2.avi'
num = 10

cap = cv2.VideoCapture(filename)
cap1 = cv2.VideoCapture(filename1)
img2 = cv2.imread("Result/key.png")

ret, slave = cap.read()
ret, slave1 = cap1.read()
shape = slave.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('Result/result.avi',fourcc, 30.0, (int(shape[1]),int(shape[0])))

while(ret):
	img = decrypt(slave, slave1, img2, num)
	out.write(np.uint8(img))
	ret, slave = cap.read()
	ret, slave1 = cap1.read()
	print "Doing.... "

cap.release()
cap1.release()
out.release()

