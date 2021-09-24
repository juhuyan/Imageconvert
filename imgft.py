# -*- coding: utf-8 -*-
"""
Created on Mon May 25 09:27:27 2020
(1) Resize image to 512*512
(2)change image format to .jpg/.png

@author:
"""

# -*- coding: utf-8 -*-
from PIL import Image
import os.path
import glob
def convertjpg(jpgfile,outdir,width=512,height=512):
    img=Image.open(jpgfile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
    except Exception as e:
        print(e)
for jpgfile in glob.glob("C:\\PaddleSeg\\data\\histopathology_dataset\\testImg\\*.jpg"):
    convertjpg(jpgfile, "C:\\PaddleSeg\\data\\histopathology_dataset\\testImg")