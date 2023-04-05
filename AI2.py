import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
image = cv2.imread("Njoud.jpg")
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imwrite("photo.jpg", gray)
cv2.imshow('photo', image)
I = cv2.waitKey(0)
if I == 27 or I == ord ('s'):
    cv2.destroyAllWindows()