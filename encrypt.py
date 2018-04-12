import cv2
import numpy as np

def encrypt(slave, img2, num):
	shape = slave.shape
	a = np.ones(shape)
	a = np.multiply(num, a)
	temp = np.subtract( np.multiply(a , img2), slave)
	img = np.floor_divide(temp, np.subtract(img2, a)) 
	img1 = np.remainder(temp, np.subtract(img2, a))
	return img, img1


