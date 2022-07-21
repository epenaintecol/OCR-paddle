from paddleocr import PaddleOCR,draw_ocr
import os
import cv2
import matplotlib.pyplot as plt
from skimage.filters.rank import entropy
from skimage.morphology import disk
import numpy as np
from skimage.filters import threshold_otsu
from scipy.ndimage.filters import uniform_filter
from scipy.ndimage.measurements import variance
import re
import cv2
import glob

def lee_filter(img, size):
    img_mean = uniform_filter(img, (size, size))
    img_sqr_mean = uniform_filter(img**2, (size, size))
    img_variance = img_sqr_mean - img_mean**2

    overall_variance = variance(img)

    img_weights = img_variance / (img_variance + overall_variance)
    img_output = img_mean + img_weights * (img - img_mean)
    return img_output

def shape(lst):
    length = len(lst)
    shp = tuple(shape(sub) if isinstance(sub, list) else 0 for sub in lst)
    if any(x != 0 for x in shp):
        return length, shp
    else:
        return length

def obtenerTextoYPresicion(resultadoOCRPaddle):
    texto=[]
    presicion=[]
    for result in resultadoOCRPaddle:
        texto.append(result[-1][0])
        presicion.append(result[-1][1])
    return texto,presicion

def concatenarLosTextos(textoList):
    textoTotal=""
    for i in textoList:
        if len(re.findall('[0-9]+', i))!=0:
            textoTotal=textoTotal+i+" "
    return textoTotal

def rectangle(img):
    gray = img[:,:,0]
    mask = cv2.inRange(gray, 0, 35) 
    kerneldilation = np.ones((45,45), np.uint8)

    img_dilation = cv2.dilate(mask, kerneldilation)
    cnts = cv2.findContours(img_dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        print(x,y,w,h)
        if w>550 and h>250 and y<900:
            rectangleMask = np.zeros(gray.shape,np.uint8)
            rectangleMask[y:y+h,x:x+w] = gray[y:y+h,x:x+w]
    return rectangleMask


ocr = PaddleOCR(use_angle_cls=True, detection=False)
i=0
for img in glob.glob("Imagenes/FLA tapa/tapa/solo verde y verde con 50 de rojo/*.png"):
    i=i+1
    limInf=0
    limSup=10
    if i>=limInf and i<=limSup:
        cv_img = cv2.imread(img)
        #gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY)
        
        #hsv_img = cv2.cvtColor(cv_img, cv2.COLOR_BGR2HSV)
        #canal=hsv_img[:,:,2]
        # #dst = cv2.fastNlMeansDenoising(canal,None,12,10,7,21)
        # #filtrada=lee_filter(canal, 4)
        #filtrada=cv2.medianBlur(canal, 21)
        # #edges = cv2.Canny(canal,40,40)
        #resta=canal-filtrada
        # # = cv2.Canny(resta,40,40)
        # entropy_imge=entropy(resta, disk(2))
        #thresh = threshold_otsu(edges)
        #Now let us binarize the entropy image 
        #binary = (edges >= thresh).astype('uint8')
        # ret2,thresh = cv2.threshold(canal,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #mask = cv2.inRange(resta, 200, 255) 
        #vis = np.concatenate((resta, gray), axis=1) 
        cutedImage=rectangle(cv_img) 
        #gray = cv_img[:,:,0]
        #mask = cv2.inRange(cutedImage, 0, 40) 
        #ret2,mask = cv2.threshold(cutedImage,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU) 
        #mask_negative=cv2.bitwise_not(mask)
        #mask_negative=mask
        result = ocr.ocr(cutedImage)

        #resized = cv2.resize(cv_img[:,:,0], (512,512), interpolation = cv2.INTER_AREA)
        texto,presicion=obtenerTextoYPresicion(result)
        titulo=concatenarLosTextos(texto)
        print("\r\r\r\r\r")
        print(texto)
        print(presicion)        
        
        #cv2.imshow("Nombre",resized)
        #cv2.waitKey()
        plt.figure(i)
        plt.imshow(cutedImage,cmap='gray')
        plt.title(titulo)

# for j in result:
#     print("fila")
#     print(len(result))
#     for h in j:
#         print("columna")
#         print(type(h))
#         print(h)



plt.show()


#
#result = ocr.ocr(r"C:\Users\INTECOL\Documents\Edier\OCR_Paddle\Imagenes\pil_text_font.png")
#print(result)
#a=15





    



