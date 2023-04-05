
import cv2

camera = cv2.VideoCapture(0)

while(True):
    
    ret, frame = camera.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):
        break

camera.release()
cv2.destroyAllWindows()