import cv2
import numpy as np

def decrypt(img, img1, img2, num):
	shape = img.shape
	a = np.ones(shape)
	a = np.multiply(num, a)
	img3 = np.subtract(np.multiply(a, img2) , np.add(np.multiply(np.subtract(img2, a) , img)  , img1))
	return img3


