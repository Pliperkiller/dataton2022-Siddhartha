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



Fase participación: La participación se divide en 3 escenarios:

1. El nombre de la entidad es mencionado en el título o en el contenido de la noticia, si esto se cumple entonces se marca como cliente.
2. El sector al que pertenece la noticia (columna sector) se menciona en el título o en el contenido de la noticia, si esto se cumple entonces se marca como sector.
3. No aparece ni el nombre de la entidad ni el sector, por lo tanto no hay participación y se marca como no aplica

Para esto se creo un iterrows, el cual barre cada fila y nos entrega un indice y la misma fila. En este ciclo se crearon los condicionales anteriores para marcar que tipo de participación se tiene.

Fase recomendación: Se tomaron cada una de las filas que hacen referencia al sector y se realizó una concatenación, y con ayuda de la libreria regex de python, eliminamos los caracteres numericos. Este mismo proceso se realiza para el título de la noticia y el contenido de la misma.
Se realizó una tokenización de todas las columnas del dataframe clientes con el fin de realizar un conteo de las palabras que hay en cada columna y encontrar las palabras mas influyentes en cada uno de los casos.

Se toman finalmente los tokens de las noticias, eliminando las palabras duplicadas y los stop words. Creamos una función llamada token influence para calcular las palabras que mas se repiten en la noticia.


