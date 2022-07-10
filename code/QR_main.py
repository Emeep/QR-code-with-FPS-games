import cv2
import numpy as np
import win32api, win32con

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

from QRdetection_cv import scan
from QR_move import inputs

while True:
    success, img = cap.read()

    text = scan(img)

    inputs(text)

    cv2.imshow('igm', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
exit()