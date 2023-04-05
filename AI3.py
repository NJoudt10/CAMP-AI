import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
img = cv2.imread("nj.jpg")
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
des = cv2.cornerHarris(gray , 2,5,0.07)
des = cv2.dilate(des,None)
imag = [des  > 0.01 * des.max()] [0 ,0 , 255]
plt.imshow(img)
plt.waitforbuttonpress

