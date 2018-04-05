import numpy as np
import cv2
import math


#opdracht 4
def moertjes():
    img = cv2.imread('bouten_moeren.jpg')
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(imgray,(5,5),0)
    ret, th = cv2.threshold(blur,180,255,cv2.THRESH_BINARY_INV)
    image, contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print hierarchy

    hierarchy = hierarchy[0]

    for cnr in range(len(contours)):
        cnt = contours[cnr]

        area = cv2.contourArea(cnt)
        perimeter = cv2.arcLength(cnt,True)
        factor = 4 * math.pi * area / perimeter**2

        holes = 0
        child = hierarchy[cnr][2]
        while child >= 0:
            holes += cv2.contourArea(contours[child])
            child = hierarchy[child][0]
            
        print area, factor, holes

        #Liggend moertje
        if(holes > 0):
            img = cv2.drawContours(img, [cnt], -1, (255,0,0), 3)
        #Liggend boutje
        elif(area > 3600):
            img = cv2.drawContours(img, [cnt], -1, (0,255,255), 3)
        #Staand moertje
        elif(area > 600 and area < 1500):
            img = cv2.drawContours(img, [cnt], -1, (0,0,255), 3)
        #Staand boutje
        elif(area > 1500):
            img = cv2.drawContours(img, [cnt], -1, (0,255,0), 3)
    
    cv2.imshow('img', img)
    k = cv2.waitKey(0)
    print k
    cv2.destroyAllWindows()

    
moertjes()
