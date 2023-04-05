import cv2
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

image = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg', stream=True).raw)
image = image.resize((450,250))
image_arr=np.array(image)

grey = cv2.cvtColor(image_arr,cv2.COLOR_BGR2GRAY)


blur = cv2.GaussianBlur(grey,(5,5),0)
Image.fromarray(blur)

dilated = cv2.dilate(blur,np.ones((3,3)))
Image.fromarray(dilated)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))
closing = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)
Image.fromarray(closing)


car_src = 'haarcascade_car.xml'
car = cv2.CascadeClassifier(car_src)
cars = car.detectMultiScale(closing, 1.1, 1)


cnt = 0
for(x,y,w,h) in cars:
    cv2.rectangle(image_arr,(x,y),(x+w,y+h),(255,0,0),2)
cnt += 1
print(cnt,"CARS")
Image.fromarray(image_arr)

cv2.imshow('image',image_arr)
cv2.waitKey()
cv2.destroyAllWindows()