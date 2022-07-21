<h1 align="center">OCR usando Paddlepaddle</h1>

<p>
    <b>Realizado por:</b> Edier Peña
</p>

<p>Aquí se presenta un demo de OCR con el proyecto de github paddlepaddle, incluyendo la preparacion del ambiente y entrenamiento con un dataset propio</p>

## Quik start

La manera mas sencilla de usar paddleocr es importando la libreria y aplicarla directamente sobre una imagen. Para ello se debe crear un ambiente virtual con python 3.7 [1].
 
    conda create -n myenv python=3.7 

instalar la version 2.1.2 de paddlepaddle y la version 2.0.1 de paddleocr[2]
 
    pip install paddlepaddle==2.1.2
    pip install paddleocr==2.0.1

El instalar otras versiones puede traer inconvenientes.
La libreria paddlepaddle esta disponible tanto para cpu como para gpu, esta ultima tiene mas requerimientos que se trataran mas adelante, por lo que por ahora se usara la version para cpu.

Una vez instaladas las librerias se pueden usar en el codigo[3]
 
    from paddleocr import PaddleOCR
    import cv2
    ocr = PaddleOCR(use_angle_cls=True)

Alli se inicializa PP-OCRv3 y todos los pesos van a ser descargados automaticamente. Este paquete provee todos los modelos del sistema que son <i>detección<i>, <i>clasificacion de angulo<i> y <i>reconocimiento<i>.
Algunas de las funcionalidades que se le pueden configurar a esta libreria son

<ul>

<li> lang: The language which we want to recognise is passed here. For example, en for English, ch for Chinese, french for French, etc. The OCR can recognise English and Chinese by default.</li>
<li> rec_algorithm: Takes the recognition algorithm to be used as arguments. The OCR uses CRNN as its default recognition algorithm.</li>
<li> det_algorithm: Takes the text detection algorithm to be used as arguments. The OCR uses a DB text detector as its default detector. </li>
<li> use_angle_cls: Specifies if angle classifier is to be used or not and takes bool as the argument. </li>

</ul>

Finalmente se le ingresa la imagen para obtener el resultado
 
    result = ocr.ocr(img_path)
    print(result)

la imagen ultilizada de prueba es la siguiente

<div align="center">
    <img src="imagenesReadme\18459975-2021-08-30-112241.bmp"><img>
    <p align="center"><b>Figura 1.</b> Imagen de prueba</p>
</div>

El resultado que se obtiene es una lista con varios elementos internos, se subrayan en color rojo el string para facilitar la visualización del resultado.
<div align="center">
    <img src="imagenesReadme\resultadoocr.png"><img>
    <p align="center"><b>Figura 2.</b> Resultado OCR</p>
</div>

o mediante codigo separar las componentes de la lista que nos interesan como puede ser el texto y la precision
 
    def obtenerTextoYPresicion(resultadoOCRPaddle):
        texto=[]
        presicion=[]
        for result in resultadoOCRPaddle:
            texto.append(result[-1][0])
            presicion.append(result[-1][1])
        return texto,presicion

obteniendo el siguiente resultado

<div align="center">
    <img src="imagenesReadme\resultadoocr1.JPG"><img>
    <p align="center"><b>Figura 3.</b> Resultado del OCR depurado</p>
</div>
Se puede notar que salvo algunos errores, se tiene una buena estimacion del texto.

## Entrenamiento de dataset propio

Como ya se vió el resultado no es 100% efectivo, esto puede ser mas notorio con algun tipo de letra, para mejorar esto, se puede entrenar el modelo con imagenes propias, las imagenes utilizadas se pueden organizar de la siguiente manera

<div align="center">
    <img src="imagenesReadme\estructuracarpeta.png"><img>
    <p align="center"><b>Figura 4.</b> Estructura de carpetas para el entrenamiento</p>
</div>

Donde train es la carpeta que contiene las imagenes de entrenamiento y eval la carpeta que contiene las imagenes de validacion, los archivos de texto rec_gt_train.txt contienen los paths de todas las imagenes de la carpeta train con su respectiva etiqueta y rec_gt_val.txt contiene los paths de todas las imagenes de la varpeta eval con su respectiva etiqueta. En las imagenes se puede ver el ejemplo de la organizacion.

<div align="center">
    <img src="imagenesReadme\imagenestrain.png"><img>
    <p align="center"><b>Figura 5.</b> Imagenes alamacenadas en la carpeta train</p>
</div>

<div align="center">
    <img src="imagenesReadme\textotrain.png"><img>
    <p align="center"><b>Figura 6.</b> Contenido del archivo rec_gt_train.txt</p>
</div>

<div align="center">
    <img src="imagenesReadme\imageneseval.png"><img>
    <p align="center"><b>Figura 7.</b> Imagenes alamacenadas en la carpeta eval</p>
</div>

<div align="center">
    <img src="imagenesReadme\textoeval.png"><img>
    <p align="center"><b>Figura 8.</b> Contenido del archivo rec_gt_val.txt</p>
</div>

Cabe aclarar que los paths de las imagenes estan en relativo, por eso son tan cortos, además, a pesar de que las imagenes almacenadas en las carpetas se ven similares, son diferentes. La separacion entre el path de cada imagen y su respectiva etiqueta, se hace mediante <i>tabulado<i>, no <i>espacio<i>, si no se hace de esta manera, se obtendra error de entrenamiento.
Tambien es posible usar palabras enteras en las etiquetas, por ejemplo:

<div align="center">
    <img src="imagenesReadme\trainingexample.png"><img>
    <p align="center"><b>Figura 9.</b> Ejemplo de etiquetado con palabras (tomado de [4])</p>
</div>

## Preparacion del GPU

Debido a que el entrenamiento toma bastantes recursos del computador, es una buena idea usar GPU. Para que esta funciones con paddle se debe instalar CUDA 10.1 / CUDA 10.2, cuDNN 7.6. Un tutorial que permite dicha instalacion se encuentra en [5].

## Preparacion del dataset

### Split folders
Una herramienta que permite dividir nuestros datasets en train, eval y test se encuentra en [6].

### Preprocesamiento

Para dejar un dataset mas adecuado a las necesidades de la empresa, se utilizaron unas imagenes de la FLA, dichas imagenes quedaron almacenadas en el pc neo en la carpeta
 
    C:\Users\INTECOL\Documents\Edier\ImagenesOCR_Paddle\Imagenes\FLA tapa\tapa\solo verde y verde con 50 de rojo

Un ejemplo de dichas imagenes se muestra a continuacion

<div align="center">
    <img src="imagenesReadme\Tapa4687.png"><img>
    <p align="center"><b>Figura 10.</b> Imagen para entrenamiento</p>
</div>

El codigo preprocesing.py muestra cuales serian las operaciones necesarias para recortar la imagen de manera que solo sea visible la parte de los carateres de interes, este se puede usar para otras imagenes similares y combinar con otras funcionalidades para crear el dataset, las operaciones que se hacen sobre la imagen son las sigueintes:

- Seleccionar el canal de mayor contraste entre los caracteres y el fondo
- Segmentación
- Dilatacion para juntar los caracteres de manera que delimiten una zona
- Encontrar el rectangulo que delimita dicha zona
- Evaluar la imagen original en el rectangulo encontrado

<div align="center">
    <img src="imagenesReadme\preprocesing.png"><img>
    <p align="center"><b>Figura 11.</b> Preprocesameinto de la imagen</p>
</div>

El codigo preparandoDataSet.py retoma todas las funcionalidades de preprocesing.py y se adecua de manera mas especifica al problema de manera que se puedan separar las dos cadenas de caracteres y ademas de etiquetar las imagenes y guardarlas. El proceso seria de la siguiente forma:
- Se le recorta a la imagen la primer cadena de caracteres

<div align="center">
    <img src="imagenesReadme\primeraCadenaDeCaracteres.png"><img>
    <p align="center"><b>Figura 12.</b> Primer cadena de caracteres recortada</p>
</div>

- El usuario debe recordar dicha cadena y cerrar manualmente la imagen
- Una vez cerrada, en la consola aparecerá el letrero "ingresa el texto que vez en la imagen: "

<div align="center">
    <img src="imagenesReadme\peticiondeingresodetexto.png"><img>
    <p align="center"><b>Figura 13.</b> Ingreso de etiqueta por consola</p>
</div>

- El usuario debe ingresar la cadena de caracteres que habia visto en la imamgen
- En caso de que el usuario no reconozca los caracteres mostrados en la imagen, la imagen no haya sido recortada correctamente o por algun motivo no desee etiquetar esa imagen puede ingresar la letra "r", en este caso la imagen no sera etiquetada ni guardada. Cabe aclarar que esta letra fue escogida ya que no se usaba en ninguna de las imagenes, sin embargo esto puede ser modificado en el codigo.
- Una vez ingresada la cadena de caracteres, la imagen sera guardada incluyendo en su nombre de archivo, el texto que el ususario ingresó, esto sera utilizado mas adelante para poner las etiquetas en un archivo txt.
- El proceso se repite para la segunda cadena de caracteres.

<div align="center">
    <img src="imagenesReadme\segundaCadenaDeCaracteres.png"><img>
    <p align="center"><b>Figura 14.</b> Segunda cadena de caracteres</p>
</div>

Una vez se tienen las imagenes nombradas y guaradas, se deben poner los respectivos paths con sus respectivas etiquetas en un archivo de texto, esto se hizo mediante el script folders.py, en este redme se mostrará el ejemplo de como se uso para las imagenes de un solo caracter:
- Las imagenes se encontraban separadas en carpetas, cada carpeta contenia un caracter diferente

<div align="center">
    <img src="imagenesReadme\estructuradecarpeta.png"><img>
    <p align="center"><b>Figura 15.</b> dataset de caracteres individuales</p>
</div> 

debido a esto se usaron dos ciclos <i>flor<i> anidados, uno para iterar sobre las carpetas y otro para iterar sobre las imagenes que hay en cada una de las carpetas.
- Dentro del criclo <i>flor<i> hay lineas que permiten tomar el nombre de la imagen sin extension, de este nombre se toma unicamente el primer caracter de la siguiente forma

    (os.path.splitext(file_name)[0])[0]

para el caso de las imagenes donde la etiqueta no es un solo caracter, sino varios, de debe hacer la debida indexacion, por ejemplo para la imagen mostrada en la figura 12, su etiqueta se compone de seis caracteres, por ende la linea de codigo se cambia de la sigueinte forma

    (os.path.splitext(file_name)[0])[:6]

de esta forma el script puede ser modificado segun la necesidad o simplemente tomado como referencia para sus propios scripts, un posible resultado de ejecutar dicho script se puede vizualizar en la figura 8.


## Entrenamiento

Una vez se tiene el dataset preparado como se muestra en la figura 4, se puede entrenar usando una sola tarjeta del gpu con el comando [4]
 
    python tools/train.py -c configs/rec/rec_icdar15_train.yml

Esto genera un archivo con los pesos de la red neuronal en la carpeta [4]
 
    C:\Users\INTECOL\Documents\Edier\OCR_Paddle\output\rec\ic15

## Evaluacion

Para evaluar el modelo se puede usar el comando [4]
 
    python -m paddle.distributed.launch --gpus '0' tools/eval.py -c configs/rec/rec_icdar15_train.yml -o Global.checkpoints={path/to/weights}/best_accuracy

## Predicción

Para ver como actua el modelo sobre una sola imagen se puede usar el comando [4]
 
    python tools/infer_rec.py -c configs/rec/rec_icdar15_train.yml -o Global.pretrained_model={path/to/weights}/best_accuracy Global.load_static_weights=false Global.infer_img=doc/imgs_words/en/word_1.jpg

## Notas

Debido al espacio de almacenamiento que permite github, este repositorio no posee el dataset que se uso para el entrenamiento, si quiere usar dichas imagenes, se encuentran en el pc NEO del laboratorio en la capeta
 
    C:\Users\INTECOL\Documents\Edier\ImagenesOCR_Paddle



## Bibliografia

[1] https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/environment_en.md

[2] https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.5/doc/doc_en/quickstart_en.md

[3] https://learnopencv.com/optical-character-recognition-using-paddleocr/?ck_subscriber_id=378289151

[4] https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.4/doc/doc_en/recognition_en.md#Custom_Dataset

[5] https://medium.com/geekculture/install-cuda-and-cudnn-on-windows-linux-52d1501a8805

[6] https://pypi.org/project/split-folders/



