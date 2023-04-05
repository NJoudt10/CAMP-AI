import cv2
image = cv2.imread("Njoud.jpg")
cv2.imshow('photo', image)
I = cv2.waitKey(0)
if I == 27 or I == ord('s'):
    cv2.destroyAllWindows()