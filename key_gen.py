import cv2
import numpy as np

def keyGen(shape, num):
	key = np.random.uniform(2*num,255,shape[0]*shape[1]*shape[2])
	img = key.reshape(shape[0], shape[1], shape[2])       
	cv2.imwrite("Result/key.png", img)


