import os
import numpy as np
import cv2
from PIL import Image
import io
#可以将标注精灵的32位图转换成8位的灰色图用于hrnet训练
#traindir="./data/mask/"
traindir=r'C:/PaddleSeg/data/histopathology_seg/Annotations/'

def convert_to_mask():

    file_list = os.listdir(traindir)
    print(file_list)
    for atom in file_list:
        #np.set_printoptions(threshold='nan')
        imname = traindir + atom
        # print(imname)
        im = cv2.imread(imname,0)
        print(imname)
        # print(im[:, :])
        print(im.shape)
        print(im.dtype)
        print("-------------after-----------------")
        cv2.imwrite(imname, im)
        #img = (im * 255).astype(np.uint8)
        _, im_th = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY)#原始的从标注精灵直接得到的png
        imnot=cv2.bitwise_not(im_th,im_th)
        _, im_th = cv2.threshold(imnot, 0, 1, cv2.THRESH_BINARY)  # 原始的从标注精灵直接得到的png
        #_, im_th = cv2.threshold(im, 128, 1, cv2.THRESH_BINARY)#之前用128转的png
        cv2.imwrite(imname, im_th)#要先保存成图片再用PIL去读才不会出现标注颜色不同的问题

        def get_color_map_list(num_classes):
            """ Returns the color map for visualizing the segmentation mask,
                which can support arbitrary number of classes.
            Args:
                num_classes: Number of classes
            Returns:
                The color map
            """
            color_map = num_classes * [0, 0, 0]
            for i in range(0, num_classes):
                j = 0
                lab = i
                while lab:
                    color_map[i * 3] |= (((lab >> 0) & 1) << (7 - j))
                    color_map[i * 3 + 1] |= (((lab >> 1) & 1) << (7 - j))
                    color_map[i * 3 + 2] |= (((lab >> 2) & 1) << (7 - j))
                    j += 1
                    lab >>= 3

            return color_map

        color_map = get_color_map_list(256)

        im = Image.open(imname)
        lbl = np.asarray(im)
        lbl_pil = Image.fromarray(lbl.astype(np.uint8), mode='P')
        lbl_pil.putpalette(color_map)
        lbl_pil.save(imname)
        # #lbl_pil.save(imname.replace("_1",""))


        #_, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)
        # blur = cv2.GaussianBlur(im, (5, 5), 0)
        # ret3, im_th = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # print(img.shape)

        # print(im_th.shape)
        # print(im_th.dtype)
        # print(im_th[ :, :])
        # print(item[:-5] + ".png")
        #cv2.imwrite(imname.replace("_1",""), im_th) #能用的版本
        #cv2.imwrite(imname, im_th)




if __name__ == '__main__':
    convert_to_mask()