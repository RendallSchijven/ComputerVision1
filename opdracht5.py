import numpy as np
import cv2
import math


#opdracht 5
def moertjes():
    img = cv2.imread('dobbelstenen.png')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret, thresh = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    dotCount = []

    dots = 0
    for cnr in range(len(contours)):
        x,y,w,h = cv2.boundingRect(contours[cnr])
        die = img[y:y+h, x:x+w]

        grayDie = cv2.cvtColor(die, cv2.COLOR_BGR2GRAY)
        blurDie = cv2.GaussianBlur(grayDie, (5,5), 0)
        retDie, threshDie = cv2.threshold(blurDie, 228, 255, cv2.THRESH_BINARY_INV)
        imageDie, contoursDie, hierarchyDie = cv2.findContours(threshDie, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        for cnrr in range(len(contoursDie)):
            cntDie = contoursDie[cnrr]
            area = cv2.contourArea(cntDie)
            perimeter = cv2.arcLength(cntDie,True)
            factor = 4 * math.pi * area / perimeter**2

            if(factor > 0.8):
                dots += 1
        if(dots < 7):
            dotCount.append(dots)
        dots = 0
    dotCount.sort()
    print dotCount

    
moertjes()
