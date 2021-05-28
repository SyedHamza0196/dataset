import cv2
import random
import os

images = os.listdir("/home/macho/Desktop/tmp_work/pioneer_augmentation/org-images/all/")
overlays = os.listdir("/home/macho/Desktop/tmp_work/pioneer_augmentation/test/overlay/")
for image in images:
    eo = int(os.path.splitext(image)[0])
    if int(eo) % 2:
        x_offset = random.randint(0,200)
        y_offset = random.randint(0,1000)
    else:
        x_offset = random.randint(1600,1800)
        y_offset = random.randint(0,1000)
    
    overlay_index = random.randint(0,len(overlays)-1)
    small = cv2.imread("./test/overlay/"+overlays[overlay_index])
    # stool = cv2.resize(stool, (0,0), fx=4, fy=4)
    # x_offset=y_offset=50
    img = cv2.imread("./org-images/all/"+image)
    img[y_offset:y_offset+small.shape[0], x_offset:x_offset+small.shape[1]] = small
    cv2.imwrite("/home/macho/Desktop/tmp_work/pioneer_augmentation/variations/overlay/"+image,img)