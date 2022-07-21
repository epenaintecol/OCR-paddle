from paddleocr import PaddleOCR
import cv2

def obtenerTextoYPresicion(resultadoOCRPaddle):
    texto=[]
    presicion=[]
    for result in resultadoOCRPaddle:
        texto.append(result[-1][0])
        presicion.append(result[-1][1])
    return texto,presicion

ocr = PaddleOCR(use_angle_cls=True)

result = ocr.ocr(r"C:\Users\JAC\Documents\2.EDIER\ocrPaddleDocumentacion\imagenesReadme\18459975-2021-08-30-112241.bmp")

print("Resultado", result)

texto, precision=obtenerTextoYPresicion(result)

print("texto: ",texto)
print("presicion; ",precision)