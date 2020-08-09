##import cv2
##
##for i in range(1,5):
##    image = cv2.imread("z"+str(i)+".jfif")
##    resized = cv2.resize(image, (400,300), interpolation = cv2.INTER_AREA)
##    cv2.imshow("n"+str(i), resized)
##    cv2.imwrite("n"+str(i)+".jpg",resized)
##
##       
##cv2.waitKey(0)

import cv2
import numpy as np

if __name__ == '__main__' :

    # Read image
    im = cv2.imread("n1.jpg")
    
    # Select ROI
    r = cv2.selectROI(im)
    
    # Crop image
    imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    # Display cropped image
    cv2.imshow("Image", imCrop)
    cv2.waitKey(0)
