import os
os.environ['DISPLAY'] = ':0'
import cv2

counter = 0
mask_y = 0
masked_path = "/home/server1/hamza/tmp_work/mask/masked/"

images = os.listdir("/home/server1/hamza/tmp_work/mask/image/")
print(images, )
for image in images:
    img, _ = os.path.splitext(image)
    with open("/home/server1/hamza/tmp_work/mask/label/"+img+".txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.split()[0] == "1":
                print(line)
                mask_y = int(float(line.split()[2]) + float(line.split()[4]))
                print(mask_y)
    counter = counter + 1
    
    img_ = cv2.imread("/home/server1/hamza/tmp_work/mask/image/" + img+".jpg")
    start_point = (0, mask_y)
    end_point = (2303, 1295)
    color = (0, 0, 0)
    thickness = -1
    img_ = cv2.rectangle(img_, start_point, end_point, color, thickness)
    cv2.imwrite(masked_path+img+".jpg", img_)
    # cv2.waitKey(0)