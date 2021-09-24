from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


###############################################################tif->jpg/png

path_name = r'C:\\PaddleSeg\\data\\histopathology_dataset_convert2\\annotations'  #原图片所在路径
# out_gray_HR = '/home/server109/ADAXI/code/PyCharm_Projects/train_gray_HR'
# out_gray_LR = '/home/server109/ADAXI/code/PyCharm_Projects/train_gray_LR'
i = 0
for item in os.listdir(path=path_name):
    new_item = str(i)+'.jpg'  #original image
    os.rename(os.path.join(path_name, item), os.path.join(path_name, new_item))
    file_path = os.path.join(path_name, new_item)
    out_path = os.path.splitext((file_path))[0] + '.png'
    print(out_path)
    Image.open(file_path).save(out_path)
    os.remove(os.path.join(path_name, new_item))
    i+=1
print("finish rename")