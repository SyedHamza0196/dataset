import cv2
import numpy as np
import os

images = os.listdir("/home/hamza/MEGA/pioneer_plate/new_tagging_29042021/images/")

for image in images:
    #-----Reading the image-----------------------------------------------------
    img = cv2.imread("/home/hamza/MEGA/pioneer_plate/new_tagging_29042021/images/"+image, 0)

    final = cv2.equalizeHist(img)
    
    cv2.imwrite("/home/hamza/MEGA/pioneer_plate/new_tagging_29042021/hist/images/"+image,final)