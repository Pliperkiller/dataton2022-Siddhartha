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

Fase clasificador: Nuestro clasificador se basa en un modelo de aprendizaje supervisado. Inicialmente se creo un archivo llamado Url noticias clasificadas el cual se encuentra en \src\data\archivos_auxiliares\url_noticias_clasificadas.xlsx y contiene dos columnas, una primera columna con la URL de noticias y una segunda columna con la clasificación de cada una de estás, este documento se creo con el objetivo de brindarle al programa un diccionario lexico que le permite determinar con que frecuencia se utilizan cierta cantidad de palabras o palabras especificas. Luego de tener el archivo, realizamos un proceso de webscrapping con ayuda de la libreria Beautifulsoup de Python, para utilizar esta libreria de una manera automatica creamos una función para cada una de las páginas web utilizadas, esta función se encuentra en ela rchivo url_config.py y es llamada en el código principal para usarla en el proceso de entrenamiento.

Para realizar el entrenamiento, se hace uso de un modelo Bayesiano, el cual hace parte de la libreria NLTK. Se utiliza este particularme por la rapidez de procesamiento del mismo y la velocidad de entrenamiento, así como también, por la facilidad que ofrece para programar los features de reconocimiento de la información que se ingresa.

Los parametros de entrenamiento son:

1. top_freqdist: Corresponde con el top 100 de las palabras mas frecuentes dentro del texto y que son diferentes a las stopwords.
2. top_2gram: Este parametro corresponde a una lematizacion, a partir de bigramas y calcula los mas frecuentes dentro del texto.
3. top_3gram: Este parametro corresponde a una lematizacion, a partir de trigramas y calcula los mas frecuentes dentro del texto.
4. top_4gram: Este parametro corresponde a una lematizacion, a partir de 4-gramas y calcula los mas frecuentes dentro del texto.
5. Vocab: Imprime el vocabulario que tiene el texto.
6. toklen: Imprime la cantidad de tokens que tiene la noticia.

Fase participación: La participación se divide en 3 escenarios:

1. El nombre de la entidad es mencionado en el título o en el contenido de la noticia, si esto se cumple entonces se marca como cliente.
2. El sector al que pertenece la noticia (columna sector) se menciona en el título o en el contenido de la noticia, si esto se cumple entonces se marca como sector.
3. No aparece ni el nombre de la entidad ni el sector, por lo tanto no hay participación y se marca como no aplica

Para esto se creo un iterrows, el cual barre cada fila y nos entrega un indice y la misma fila. En este ciclo se crearon los condicionales anteriores utilizando un "for in" en cada fila de las columnas nombre, subsec y news_title para marcar que tipo de participación se tiene para cada noticia.

Fase recomendación: Se realizó una tokenización de todas las columnas del dataframe clientes con el fin de realizar un conteo de las palabras que hay en cada columna y encontrar las palabras mas influyentes en cada uno de los casos. Se tomaron cada una de las filas que hacen referencia al sector y se realizó una concatenación de las columnas: 'desc_ciiu_division','desc_ciuu_grupo','desc_ciiuu_clase'. Posteriormente, con ayuda de la libreria regex de python, eliminamos los caracteres no alfabeticos. Este mismo proceso se realiza para el título de la noticia y el contenido de la misma. La tokenización se implementa utilizando la función word_tokenize de la libreria nltk.

Se toman finalmente los tokens de las noticias, eliminando las palabras duplicadas y los stop words. Creamos una función llamada token influence para calcular la frecuencia de las palabras relacionadas con la participación del cliente. Con esto obtenemos calculamos los siguientes score:

1.Un score que tiene la influencia del sector en la noticia. Si la noticia tiene 5 tokens, correspondientes al sector del cliente, se le asocia 1 punto. En caso de tener 10 tokens, se le asignan 2 puntos.

2.Un score del nombre del cliente. En el caso en el que el nombre del cliente se encuentre dentro de la noticia, asociamos, 2 puntos. De lo contrario, no se asignan puntos. 

3. Un score del sector del cliente. Sí el sector del cliente se encuentra dentro de la noticia se le asigna 1 punto. De lo contrario, no se asignan puntos.

4. Longitud de la noticia, si la longitud de la noticia es mayor o igual a 500 se le asocia 1 punto, de lo contrario, no se asignan puntos.





