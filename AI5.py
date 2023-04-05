import cv2

face_detector = cv2.CascadeClassifier('myfacedetector.xml') 

cape = cv2.VideoCapture('Elon Musk.mp4')

if not cape.isOpened():
    print("Could not open video file")
    exit()

color = (255, 0, 0)  
thickness = 5  

 
while True:
    ret, img = cape.read()

    if not ret:
        print("Could not read frame")
        break

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, thickness) 

    cv2.imshow('Video', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cape.release()
cv2.destroyAllWindows()