import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np

plt.close("all")
i=0
limInf=0
limSup=10
kernel = np.ones((70,60),np.uint8)

for img in glob.glob(r"C:\Users\JAC\Documents\2.EDIER\datasets\segmentacionFLA\soloVerdeYVerdeCon50DeRojo\solo verde y verde con 50 de rojo/*.png"):
    
    i=i+1

    #if i>limInf and i<limSup:
    imagen= cv2.imread(img)
    imagen=imagen[:,:,1]
    tresh=cv2.inRange(imagen,0,50)
    dilation = cv2.dilate(tresh,kernel,iterations = 1)

    cnts = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        if y<800 and w>550 and h>300:
            print("x: ",x)
            print("y: ",y)
            print("w: ",w)
            print("h: ",h)
            imagenRecortada1=np.zeros_like(dilation)
            imagenRecortada2=np.zeros_like(dilation)
            imagenRecortada1[y:y+int(h/2),x:x+w]=imagen[y:y+int(h/2),x:x+w]

            plt.figure(i)
            plt.imshow(imagenRecortada1,cmap='gray')
            plt.title("texto de arriba")
            plt.show()

            imagenRecortada2[y+int(h/2):y+h,x:x+w]=imagen[y+int(h/2):y+h,x:x+w]
            texto = input("ingresa el texto que vez en la imagen: ")
            print(texto)
            if texto!="r":
                cv2.imwrite("C:/Users/JAC/Documents/2.EDIER/FLA/IMAGENES/DatasetOCR"+"/"+texto+"("+str(i)+")"+".bmp", imagenRecortada1)
            
            plt.close("all")

            plt.figure(i)
            plt.imshow(imagenRecortada2,cmap='gray')
            plt.title("texto de abajo")
            plt.show()
            texto = input("ingresa el texto que vez en la imagen: ") 
            print(texto) 
            if texto!="r":
                cv2.imwrite("C:/Users/JAC/Documents/2.EDIER/FLA/IMAGENES/DatasetOCR"+"/"+texto+"("+str(i)+")"+".bmp", imagenRecortada2)
            plt.close("all")   



