
import cv2

face = cv2.CascadeClassifier('myfacedetector.xml')

camera = cv2.VideoCapture(0)

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:

    read_ok, frame = camera.read()

    if not read_ok:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('z'):
        break

camera.release()
cv2.destroyAllWindows()