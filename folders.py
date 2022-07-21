# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 09:24:29 2022

@author: INTECOL
"""

import os
import shutil
 
rootdir = r'C:\Users\INTECOL\Documents\Edier\dotDataMatrixGenerator\OCR_Expiration_Date\Custom_Dot_Matrix_Dataset\Dot_Matrix_test_edier'

with open(r'C:\Users\INTECOL\Documents\Edier\OCR_Paddle\train_data\ic15_data\rec_gt_train.txt', 'w') as f:

    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            for images in os.listdir(d):
                # file name with extension
                file_name = os.path.basename(images)
    
                # file name without extension
                print((os.path.splitext(file_name)[0])[0])
                path="train/"
                f.write(path+images)
                f.write('\t')
                f.write((os.path.splitext(file_name)[0])[0])
                f.write('\n')
                
                #shutil.copy(d+"/"+images, r"C:\Users\INTECOL\Documents\Edier\OCR_Paddle\Imagenes\train_data\rec\train")
                
                
                
                
                
