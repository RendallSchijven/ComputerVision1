import numpy as np
import cv2
import math


#opdracht 3
def moertjes():
    img = cv2.imread('bouten_moeren.jpg')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray,(5,5),0)
    ret, th = cv2.threshold(blur,180,255,cv2.THRESH_BINARY_INV)
    image, contours, hierachy = cv2.findContours(th, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
    
    cv2.imshow('img', img)
    k = cv2.waitKey(0)
    print k
    cv2.destroyAllWindows()
    
moertjes()
