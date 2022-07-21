<h1> Seguridad </h1>

## Detección de condiciones inseguras.



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Tabla de contenidos</summary>
  <ol>
    <li>
      <a href="#introduction">Introduccion</a>
    </li>
    <li>
      <a href="#install">Instalacion</a>
      <ul>
        <li><a href="#database">Base de datos y configuración</a></li>
            <ul>
            <li><a href="#SSMS">instalacion SSMS y SQLEXpress</a></li>
            <li><a href="#user">SuperUsuario SQL</a></li>
            <li><a href="#port">Habilitacion Puerto</a></li>
            <li><a href="#problems">Solucion de problemas SQL</a></li>
            <li><a href="#db">Restauracion DB</a></li>
            </ul>
        <li><a href="#program">Programa de Seguridad</a></li>
            <ul>
                <li><a href="#anaconda">Ambiente con Anaconda</a></li>
                <li><a href="#python">Ambiente con Python</a></li>
                <li><a href="#pesos">Pesos modelo Yolo</a></li>
                <li><a href="#run">Correr el programa</a></li>
                  <ul>
                    <li><a href="#runConsole">Correr detección con consola</a></li>
                    <li><a href="#runWeb">Correr deteccion en navegador</a></li>
                  </ul>
                  <li><a href="#gpu">Configuración GPU</a></li>
                  <li><a href="#cythonizar">Cythonizar</a></li>
            </ul>
        <li><a href="#Testing">Testing</a></li>
        <li><a href="#Docker">Docker</a></li>
      </ul>
    </li>


  </ol>
</details>

<p align="center">
<img src="resources/intecol.PNG"></img> 
</p>


<p id="introduction">
</p>

# Introduccion


En el marco del proyecto de identificación de eventos que atenten contra la seguridad utilizando AI en el sistema de cámaras de seguridad de VIDRIO ANDINO, INTECOL SAS desarrolló una aplicación que detecta diferentes eventos que atentan contra la seguridad del personal y realiza reportes analizando el tipo y cantidad de alarmas que ocurrió en un turno. Para hacer esto se entrenó un modelo con cerca de 30000 imágenes, dicho modelo permite detectar personas y montacargas. Una vez entrenado el modelo se procedió a detectar cada una de las siguientes alarmas: Alerta proximidad de personas o montacarga a un montacarga, Detección ausencia de chaleco, obstáculos en regiones de descargue, disposición de la malla, escaleras levantadas en el camión, persona montada en los vidrios y detección si el montacargas está prendido o apagado y está en regiones permitidas. Cada una de estas alarmas se almacena en una base de datos, se guarda la imagen que generó la alarma y al final de cada jornada (8 horas) se realiza un análisis del tipo de errores y la cantidad de ellos en dicha jornada, además se envía un correo electrónico con dicho resumen.
El proyecto fue implementado en la planta de vidrios andinos (Soacha - Cundinamarca) en la cámara muelle 4 y 5 cuya IP es 192.168.0.112, además se implementó en un servidor dispuesto por vidrios andinos. Para mas información relacionada, dirigirse al informe dirigido a Vidrios.





<p id="install">
</p>

# Instalacion


<p id="database">
</p>

# Base de datos y configuración

<p id="SSMS">
</p>

## instalacion SSMS y SQLEXpress

Es necesario descargar SQL Server Express 2019. [Descargas de SQL Server | Microsoft](https://www.microsoft.com/es-es/sql-server/sql-server-downloads). 
<p align="center">
<img src="resources/sqlexpress.PNG"></img> 
</p>


Descargar SQL Server Management Studio 18 [SSMS](https://docs.microsoft.com/es-es/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15). 

<p align="center">
<img src="resources/sqlserver.PNG"></img> 
</p>


Se procede instalar SQL express 2019, para ello hacer click en el ejecutable y seleccionar tipo de instalacion basica: 
<p align="center">
<img src="resources/sqlexpressbasica.PNG"></img> 
</p>

Se aceptan las licencias 
<p align="center">
<img src="resources/sqlexpress2.PNG"></img> 
</p>

Instalar
<p align="center">
<img src="resources/sqlexpress3.PNG"></img> 
</p>

Una vez instalado click en cerrar
<p align="center">
<img src="resources/sqlexpress4.PNG"></img> 
</p>

Se procede instalar SSMS , para ello hacer click en el ejecutable e instalar regularmente el SSMS: 
<p align="center">
<img src="resources/ssms1.PNG"></img> 
</p>

<p id="user">
</p>

## Creacion de super usuario SQL

abrir SSMS e inicia sesión en SSMS con Windows Authentication.

en la carpeta security/Logins hacer click derecho y seleccionar New Login
<p align="center">
<img src="resources/user1.PNG"></img> 
</p>

Se abre la siguiente ventana, Colocar nombre a usuario, se recomienda "intecol" y seleccionar SQL Server authentication, colocar contraseña deseada, se recomienda "intecol.123"
<p align="center">
<img src="resources/user2.PNG"></img> 
</p>

Hacer click en server Roles y habilitar la casilla de sysadmin, se recomienda habilitar todas las casillas tambien.
<p align="center">
<img src="resources/user3.PNG"></img> 
</p>

click en ok y si el usuario esta creado correctamente iniciar sesion en SSMS con windows authentication colocando el usuario y contraseña creadas.

En caso de que aparezca el error 18456 al intentar iniciar sesión:

<p align="center">
<img src="resources/user4.PNG"></img> 
</p>

 vaya a propiedades:

 <p align="center">
<img src="resources/user5.PNG"></img> 
</p>
y en security habilite SQL server and Windows Authentication mode, click ok y ya deberia poder iniciar sesion.
 <p align="center">
<img src="resources/user6.PNG"></img> 
</p>

<p id="port">
</p>

## Habilitacion Puerto

Abrir SQL server 2019 Configuration Manager y en SQL Server Network Configuration/ protocols for SQLEXpress, click derecho en TCP/IP y click en propiedades

<p align="center">
<img src="resources/sqlconf.png"></img> 
</p>

Seleccionar Enabled YES:
<p align="center">
<img src="resources/sqlconf2.PNG"></img> 
</p>
y en la pestaña IP Addresses ir hasta la parte final IPALL y en TCP Port colocar el puerto  1433

<p align="center">
<img src="resources/sqlconf3.PNG"></img> 
</p>

<p id="problems">
</p>

## Solucion de problemas SQL

Si existe un error de algun tipo luego de la instalacion o en medio de la instalacion por favor revisar los siguientes links:
- [How to Fix Login Failed Microsoft SQL Server Error: 18456](https://appuals.com/sql-server-error-18456/)
- [SQL Server does not exist or access denied error message](https://www.sqlserverlogexplorer.com/database-does-not-exist-access-denied/)
- [How-to-find-your-database-IP-address-and-SQL-port](https://amberpos.zendesk.com/hc/en-us/articles/215978723-How-to-find-your-database-IP-address-and-SQL-port)

<p id="db">
</p>

## Restauracion DB

click derecho en Databases, click Restore Database, seleccionar en source Device, hacer click en los tres puntos , seleccionar Add y buscar el backup de la base de datos mas actual.

<p align="center">
<img src="resources/db1.PNG"></img> 
</p>

 La base de datos la puede encontrar en [Base de datos/Backups](https://drive.google.com/drive/folders/1kkD8Ch9cSVf9AfqY2gAV8SXiBYEv565q?usp=sharing) 
Cabe notar que esta carpeta del drive contiene informacion util del proyecto


<p id="program">
</p>

# Programa de Seguridad

El programa lo encuentra en el correspondiente Repositorio de [github](https://github.com/dcnavarros-intecol/Seguridad).
Para obtenerlo en su computador abra el cmd o command prompt, ubiquese en la carpeta que desea tener el proyecto y corra el siguiente comando si tiene el SSH configurado correctamente,[aqui puede ver como configurar SSH](https://www.freecodecamp.org/espanol/news/como-obtener-y-configurar-tus-claves-ssh-para-git-y-github/):


        git clone git@github.com:dcnavarros-intecol/Seguridad.git 

en caso de que no use SSH corra el siguiente comando:

        git clone https://github.com/dcnavarros-intecol/Seguridad.git

La configuracion del ambiente y los paquetes necesarios puede hacerse mediante anaconda o directamente ejecutando el commando venv

<p id="anaconda">
</p>

## Anaconda:

Anaconda es una distribución de los lenguajes de programación Python y R para computación científica (ciencia de datos, aplicaciones de Machine Learning, procesamiento de datos a gran escala, análisis predictivo, etc.).

Tiene como ventaja simplificar la gestión e implementación de paquetes. La distribución incluye paquetes de “data science” adecuados para Windows, Linux y macOS. 

Para descargarlo vaya al siguiente [link](https://www.anaconda.com/products/distribution)

una vez descargado e instalado cree un nuevo ambiente, en el command prompt de anaconda cree un nuevo ambiente(puede cambiar "nombreenv" por el nombre deseado de su ambiente, se recomienda "seguridad" y python "x.x" lo puede modificar por 3.8 o 3.9):
    conda create -n nombreenv python=x.x
  
Ahora Se activa el ambiente

    conda activate nombreenv

una vez dentro del ambiente vaya dentro de la carpeta seguridad 
    cd seguridad
e instale los paquetes de python necesarios:

    pip install -r requirements.txt

<p id="python">
</p>

## Ambiente Python:

Descargue e instale [python](https://www.python.org/downloads/release/python-3912/) y añadalo al [path path del sistema](https://datatofish.com/add-python-to-windows-path/)
una vez instalado y configurado cree un nuevo ambiente y activelo:

    pip install virtualenv
    virtualenv virtualenv
    cd virtualenv\Scripts
    activate

vaya a cd Seguridad e instale los paquetes necesarios 
    pip install -r requirements.txt

<p id="pesos">
</p>

## Pesos modelo Yolo

una vez instalados los requeriments se procede a buscar los archivos entrenados, los puede encontrar en el 
[drive del proyecto](https://drive.google.com/drive/folders/1ketEkgXs2Jd2RC8iHVXNb5Q_1sfRVBYP?usp=sharing)
especificamente puede encontrar los pesos en la carpeta seguridad_/model_weights

copie dichos modelos o unicamente 512x512_DA_YoloM (ya que fue el que mejor resultados presento)

y peguelos en la carpeta seguridad/yolov5/runs/train/1024_DA_yolovM/weights/

<p id="run"></p>

## Correr el programa

<p id="runConsole">
</p>

### Correr detección con consola

una vez hecho esto vaya a la carpeta yolov5: 

    cd yolov5


y ejecute el siguiente comando:

    python detect.py --weights runs/train/512x512_DA_YoloM/weights/best.pt --img 512 --conf 0.4 --source ./data/images/example.jpg
          
deberia funcionar correctamente


Note que en el argumento source puede introducir el path a una imagen, el path a un video, folder con imagenes o puede colocar el protocolo para comunicarse con una camara ip:

      python path/to/detect.py --source path/to/img.jpg --weights yolov5s.pt --img 640
      python detect.py --weights runs/train/512x512_DA_YoloM/weights/best.pt --img 512 --conf 0.4  --source ../Seguridad_videos/Videos_nuevos/muelle4y5_10_Nov
      
To use with a camera:
      python detect.py --weights runs/train/1024_DA_yolovM/weights/best.pt --img 1024 --conf 0.4 --source rtsp://root:SDSline397@192.168.0.112/axis-media/media.amp
      python detect.py --weights runs/train/512m_DA/weights/best.pt --img 512 --conf 0.4 --source rtsp://root:SDSline397@192.168.0.112/axis-media/media.amp

Para usar con camara tenga en cuenta que se debe tener el usuario, contraseña, ip de la camara : 

    rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@IP:puerto/Streaming/channels/" + str(channel) + "02"  


    # Diferentes maneras que funcionan:
    
      stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101:554/axis-media/media.amp')
      stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/HighResolutionVideo')
      stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/live')
      stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/h264_stream')

las mas recomendadas son :

      stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101:554/axis-media/media.amp')


  #Mainstream, el tamaño de imagen es la original de la camara, la cual es muy grande y en general hace el streaming mas lento:

       stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/Streaming/Channels/101')


  #Substream, el tamaño de la imagen es de 1/4 de la original(aunque pude variar por marca):

        stream = cv2.VideoCapture('rtsp://admin:Abc12345@192.168.1.101/Streaming/Channels/102')

<p id="runWeb">
</p>

### Correr deteccion en navegador 

Para correr la aplicación web se debe emplear el archivo app.py que se encuentra en la carpeta yolov5. En este archivo se debe configurar adecuadamente los parámetros de la función run. Se debe tener en cuenta la configuración previa del modelo, y que el argumento source cambiará en el tipo de archivo a procesar. 

Luego, para ejecutar el programa y observar la interfaz se deberá usar cualquier navegador web y llamar al localhost:5000/. Esto último también lo indica la consola de Python luego de ejecutar el app.py.

<p id="gpu">
</p>

## Configuración GPU

para utilizar la GPU descargue e instale [cuda 11.6](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=11)

y corra el siguiente comando dentro de su ambiente:

    pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html

para revisar si la GPU esta funcionando correctamente se ejecuta el intérprete de Python en la command prompt, y dentro de este se
importa el módulo de torch y luego se observa si tiene disponible CUDA:

    python 
    import torch
    torch.cuda.is_available()

 debe devolver un True , si devuelve False es que no reconoce la GPU aún

<p id="cythonizar">
<p/>
    
## Cythonizar - Generar ejecutables y despliegue

Informacion acerca de teoria y por que cythonizar lo puede encontrar aca:
[boosting-python-scripts-cython](https://blog.paperspace.com/boosting-python-scripts-cython/)
[Speedup your existing Python project with Cython +30x](https://medium.com/analytics-vidhya/speedup-your-existing-python-project-with-cython-30x-1dc1ffaf147a)

Crear el ejecutable utilizando Pyinstaller:

[Pyinstaller-Manual](https://pyinstaller.org/en/stable/)
[Introduction and troubleshooting](https://pbrotoisworo.medium.com/python-and-pyinstaller-introduction-and-troubleshooting-d60f983f2bcb)

* En el proyecto se cythoniza y se genera el ejecutable con un unico script, para hacerlo 
en la consola, cuando este en la carpeta seguridad escriba:

    python cythonizar.py

se va a demorar aproximadamente 2 minutos, por favor no interrumpirlo.


una vez finalizado se habra creado una carpeta llamada *MontajeVidrio* y un archivo *MontajeVidrio.zip*

el .zip se puede llevar al computador donde se esta haciendo el despliegue. 

* una vez enviado el archivo y descomprimido, dirigirse a MontajeVidrio/ejecutable/Iniciar y abrir el archivo *config_ejecutable.json* , alli encontrará 3 lineas de codigo que debe verificar:

<p align="center">
<img src="resources/deploy1.PNG"></img> 
</p>


* En path To script debe colocar la ruta hasta la carpeta *seguridad/yolov5* de MontajeVidrio.
arreglar los slash : \ --> //.



* en *ANACONDA_CONSOLE* se debe colocar el siguiente comando:

- abrir las propiedades de anaconda prompt

<p align="center">
<img src="resources/deploy2.PNG"></img> 
</p>

Observar que en target hay una linea como la siguiente:

    %windir%\System32\cmd.exe "/K" C:\ProgramData\Anaconda3\Scripts\activate.bat C:\ProgramData\Anaconda3

- copiar el segmento:

    C:\ProgramData\Anaconda3\Scripts\activate.bat 

y pegarlo en *ANACONDA_CONSOLE*, arreglar los slash : \ --> //

* en *environment* colocar el nombre del ambiente que se esta utilizando: por ejemplo *seguridad* o *seguridadCUDA*

* hay un json igual en la carpeta MontajeVidrio/ejecutable/Iniciar/dist ,  se debe realizar el mismo procedimiento o simplemente copiar y pegar el json que ya se configuró.

* en la carpeta MontajeVidrio borrar la carpeta .git 
runs/train ,runs/detect , readme, FRONTEND ANGULAR, yolov5/data/images
 LogAlarmImages, Resumenes,

