import matplotlib.pyplot as plt

import cv2
import glob
import numpy as np


i=0
for img in glob.glob("Imagenes/FLA tapa/tapa/solo verde y verde con 50 de rojo/*.png"):
    i=i+1
    limInf=0
    limSup=10
    if i>=limInf and i<=limSup:
        cv_img = cv2.imread(img)
        gray=cv_img[:,:,0]
        mask = cv2.inRange(gray, 0, 35) 
        kerneldilation = np.ones((45,45), np.uint8)

        img_dilation = cv2.dilate(mask, kerneldilation)
        cnts = cv2.findContours(img_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            x,y,w,h = cv2.boundingRect(c)
            if w>550 and h>250 and y<850:
                rectangleMask = np.zeros(gray.shape,np.uint8)
                rectangleMask[y:y+h,x:x+w] = gray[y:y+h,x:x+w]



        

        plt.figure(i)
        plt.imshow(rectangleMask,cmap='gray')

plt.show()