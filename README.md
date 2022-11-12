Dataton 2022

NLP: Sistema recomendación noticias

Objetivo: Crear un sistema de recomendación de noticias sobre clientes corporativos que le ofrezcan al comercial información relevante, actualizada y confiable.

Para cumplir con este objetivo se desarrollará a través de Python un programa capaz de realizar la clasificación. A continuación se presenta una breve descripción del contenido que se encuentra en cada una de las carpetas del Github:

Documentación:

Esta carpeta contiene documentos:

1. Terminos y condiciones, firmado por cada miembro del equipo.
2. Limpieza_clientes, es un pdf que contiene el código de Python empleado para realizar la limpieza de la base de datos de clientes.
3. Entrenamiento_categorización 

SCR:

Contiene dos sub carpetas que a su vez contienen mas carpetas con información:

- data:
  > archivos auxiliares: Contiene un archivo de excel llamado url_noticias_clasificadas.xlsx, el cual contiene los links de las noticias clasificadas que se utilizaron                           para realizar el entrenamiento.
  
  > output: Contiene un archivo csv llamado categorizacion.csv, el cuál tiene la clasificación de las noticias proporcionadas a través de la base noticias.csv
 
 Adicionalmente contiene los tres csv proporcionados para realizar el proyecto. Los cuales son: clientes.csv, clientes_noticias.csv, noticias.csv
 
- scripts: Contiene los programas que se han desarrollado para cumplir con el objetivo. A continuación se realiza una breve descripción de los programas contenidos actualmente:

  > entrenamiento_categorizacion.ipynb: Programa que contiene una serie de funciones a través de las cuales se realiza el proceso de tokenización para las noticias y el proceso de entrenamiento del modelo Bayesiano.

  > limpieza_clientes.ipynb: Programa que realiza la limpieza de la base de datos clientes.csv, se emplean ex

  > path.xlsx: Archivo que contiene el arbol de rutas de las carpetas. Es de aclarar que siempre que se vayan a ejecutar por primera vez los notbooks es necesario eliminar este archivo.

  > prueba.ipynb: Archivo de pruebas.

  > url_config.py: Funciones con la configuración del webscrapping de varios periodicos.

  > utilitools.py: Herramientas varias. 




Fase limpieza de todos los dataframes: Cómo parte del proceso de limpieza de datos decidimos iniciar por el dataframe clientes, y realizar una limpieza a la columna del nombre de la empresa, esto con el fin de que fuera mas facil realizar una coincidencia entre el nombre y el texto de la noticia. 

Fase clasificador: Nuestro clasificador se basa en un modelo de aprendizaje supervisado. Inicialmente se creo un archivo llamado Url noticias clasificadas el cual se encuentra en... y contiene dos columnas, una primera columna con la URL de noticias y una segunda columna con la clasificación de cada una de estás, este documento se creo con el objetivo de brindarle al programa un diccionario lexico que le permite determinar con que frecuencia se utilizan cierta cantidad de palabras o palabras especificas. Luego de tener el archivo, realizamos un proceso de webscrapping con ayuda de la libreria Beautifulsoup de Python, para utilizar esta libreria de una manera automatica creamos una función para cada una de las páginas web utilizadas, esta función se encuentra en ela rchivo url_config.py y es llamada en el código principal para usarla en el proceso de entrenamiento.

Se utiliza un modelo Bayesiano

Inicialmente se crea 

Fase participación:

Fase recomendación:


