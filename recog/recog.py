import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string

# Path of working folder on Disk
#Change the "PATH TO" to the proper values.
#Src_path is the folder where you want to store the images
#ex: "media/"
#for the tesseract one, i had some trouble installing the module from pip
#so i had to download the exe from the github and point that string of code down there
#to the file path where tesseract was stored

# pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract' #   may need later ?

def ocrCard():
    # Read image with opencv
    image = Image.open("cardcap.jpg")
    image.save("cardcap.jpg", dpi=(300,300))
    image = cv2.imread("cardcap.jpg")

    # convert the image to grayscale, blur it, and find edges
    # in the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(gray,127,255,0)
    edged = cv2.Canny(gray, 75, 200)
    imCopy = image.copy()
    image, contours, hierarchy =  cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #goes from largest to smallest values
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
    cv2.imshow('draw contours',imCopy)
    cv2.imshow("Edged", edged)

    for c in contours:
    	# approximate the contour
        #this is the perimeter of the contours
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    	# if our approximated contour has four points, then we
    	# can assume that we have found our screen
        if len(approx) == 4:
            screenCnt = approx
            break
    image = cv2.bitwise_not(image)
    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    cv2.imshow("Outline", image)
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("thres2.png"))

    return result
