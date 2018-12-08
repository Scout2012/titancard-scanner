import cv2
import pytesseract
import imutils
import numpy as np
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

    image = cv2.imread("cardcap.jpg")
    rimg = imutils.resize(image, width=600)
    epsilon = 0.04

    #the image height divided by the resized height gives us the ratio
    ratio = 1 #image.shape[0]/float(rimg.shape[0])

    gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    cv2.imwrite("blurred.jpg", blurred)
    cv2.imshow("blurred", blurred)
    cv2.waitKey(0)
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    cv2.imwrite("thresh.jpg", thresh)
    cv2.imshow("thresholded", thresh)
    cv2.waitKey(0)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    count = 0
    for c in cnts:
        M = cv2.moments(c)  
        if(M["m00"] != 0):
            cX = int((M["m10"] / M["m00"]) * ratio)
            cY = int((M["m01"] / M["m00"]) * ratio)
        else:
            cX, cY = 0, 0
        period = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon * period, True)
        if len(approx) == 4:
            print(approx)
            print(count)
            count+=1
            c = c.astype("float")
            c *= ratio
            c = c.astype("int")
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
            cv2.putText(image, "card", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    	    # show the output image
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # # Read image with opencv
    # image = Image.open("cardcap.jpg")
    # #image.save("cardcap.jpg", dpi=(300,300))
    # image = cv2.imread("cardcap.jpg")
    #
    # image = cv2.medianBlur(image, 5)
    #
    # gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    # cv2.imwrite("grayimg.jpg", gray)
    # cv2.imshow('gray_image',gray)
    # cv2.waitKey(0)
    #
    # blur = cv2.GaussianBlur(gray, (31,31), 0)
    #
    # # convert the image to grayscale, blur it, and find edges
    # # in the image
    # #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # #gray = cv2.GaussianBlur(gray, (5, 5), 0)
    #
    #
    # th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    #
    # cv2.imshow('original',image)
    # cv2.imwrite("thresh.jpg", th)
    # cv2.imshow('Adaptive threshold', th)
    # cv2.waitKey(0)
    #
    #
    # offset=30
    # height,width, channels = image.shape
    # image = cv2.copyMakeBorder(image,offset,offset,offset,offset,cv2.BORDER_CONSTANT,value=(255,255,255))
    # cv2.namedWindow("Test")
    # cv2.imshow("Test", image)
    # cv2.imwrite("an91cut_decoded.jpg",image)
    # cv2.waitKey(0)
    #
    # edged = cv2.Canny(gray, 75, 200)
    #
    #
    # image, contours, hierarchy =  cv2.findContours(th, 1, 2)
    #
    #
    # #goes from largest to smallest values
    # contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
    #
    # # for c in contours:
    # # approximate the contour
    # #this is the perimeter of the contours
    #
    # # if our approximated contour has four points, then we
    # # can assume that we have found our screen
    # # if len(approx) == 4:
    # #     screenCnt = approx
    # #     cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
    # for c in contours:
    #     peri = cv2.arcLength(c, True)
    #     approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    #     print len(approx)
    #     #the approx provides a list of verices, so finding the length will give us the shape
    #     if len(approx) == 3:
    #         shape = "triangle"
    #
    # 		# if the shape has 4 vertices, it is either a square or
    # 		# a rectangle
    #     elif len(approx) == 4:
    # 		# compute the bounding box of the contour and use the
    # 		# bounding box to compute the aspect ratio
    #         (x, y, w, h) = cv2.boundingRect(approx)
    #         ar = w / float(h)
    #
    # 		# a square will have an aspect ratio that is approximately
    # 		# equal to one, otherwise, the shape is a rectangle
    #         print approx
    #         shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
    #
    # 	# if the shape is a pentagon, it will have 5 vertices
    #     elif len(approx) == 5:
    #         shape = "pentagon"
    #
    # 	# otherwise, we assume the shape is a circle
    #     else:
    #         shape = "circle"
    #
	# # return the name of the shape
    # print shape
    #
    #         # break
    #
    # cv2.imshow("contours", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    #
    # # Recognize text with tesseract for python
    # result = pytesseract.image_to_string(Image.open("thresh.jpg"))
    #
    # return result
