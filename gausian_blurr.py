import cv2
import os

images = os.listdir("/home/hamza/MEGA/pioneer_plate/new_tagging_29042021/images/")

for image in images:
    #-----Reading the image-----------------------------------------------------
    img = cv2.imread("/home/hamza/MEGA/pioneer_plate/new_tagging_29042021/images/"+image, 1)

    #-----Blurring--------------------
    final = cv2.GaussianBlur(img,(5,5),0)
    cv2.imwrite("/home/hamza/MEGA/pioneer_plate/new_tagging_29042021/blur/images/"+image,final)