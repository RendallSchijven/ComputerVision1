import numpy as np
import cv2
import math


#opdracht 1
def blauw():
    img = cv2.imread('opencv-logo-white.png')

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    cv2.imshow('res', res)
    k = cv2.waitKey(0)
    print k
    cv2.destroyAllWindows()

def groen():
    img = cv2.imread('opencv-logo-white.png')

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_green = np.array([50,50,50])
    upper_green = np.array([70,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    cv2.imshow('res', res)
    k = cv2.waitKey(0)
    print k
    cv2.destroyAllWindows()

def rood():
    img = cv2.imread('opencv-logo-white.png')

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    lower_red = np.array([0,50,50])
    upper_red = np.array([20,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img,img, mask= mask)

    cv2.imshow('res', res)
    k = cv2.waitKey(0)
    print k
    cv2.destroyAllWindows()

blauw()
groen()
rood()
