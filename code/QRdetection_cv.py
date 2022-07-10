import cv2
import numpy as np

def scan(img):
    q = cv2.QRCodeDetector()
    text, _, _ = q.detectAndDecode(img)
    
    b, poly = q.detect(img)

    if b:
        poly = np.array(poly, np.int32)
    else:
        poly = None
    
    cv2.polylines(img, poly, True, (0, 255, 0), 2)

    return text