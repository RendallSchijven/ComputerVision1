import numpy as np
import cv2
import math

#opdracht 2
def opdracht2():
    img = cv2.imread('opencv-logo-white.png')
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    image, contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[0]
    
    M = cv2.moments(cnt)
    x = int(M['m10']/M['m00'])
    y = int(M['m01']/M['m00'])
    
    hull = cv2.convexHull(cnt)
    
    img = cv2.circle(img, (x,y), 5, (0,255,255), -1)
    img = cv2.drawContours(img, [hull], 0, (0,255,255), 3)
    
    cv2.imshow('res', img)
    k = cv2.waitKey(0)
    print k
    cv2.destroyAllWindows()

opdracht2()
