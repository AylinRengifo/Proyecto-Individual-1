
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
# <h1 align=center> DATA FT17 </h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

<hr>


# Índice 
<details>
  <summary>Tabla de contenido</summary>
  <ol>
    <li><a href="#INTRODUCCION">INTRODUCCIÓN</a></li>
    <li><a href="#DATOS">DATOS</a></li>
    <li><a href="#TAREAS-DESARROLLADAS">TAREAS DESARROLLADAS</a></li>
    <li><a href="#TRANSFORMACIONES">TRANSFORMACIONES</a></li>
    <li><a href="#FEATURE-ENGINEERING">FEATURE ENGINEERING</a></li>
    <li><a href="#EDA">ANÁLISIS EXPLORATORIO DE LOS DATOS (EDA)</a></li>
    <li><a href="#MODELO-ML">MODELO ML</a></li>
    <li><a href="#DESARROLLO-API">DESARROLLO API</a></li>
    <li><a href="#CONCLUSIONES">CONCLUSIONES</a></li>
    <li><a href="#TECNOLOGIAS-USADAS">TECNOLOGÍAS USADAS</a></li>
  </ol>
</details>

</body>
</html></p>

<hr></p>


# INTRODUCCION </p>

<p style="text-align: justify;"> Este proyecto representa la simulación del papel integral de un MLOps Engineer para la reconocida plataforma internacional de juegos, Steam. Asumí roles cruciales desde la ingeniería de datos hasta el despliegue de modelos de Machine Learning, centrándome en la creación de un Producto Mínimo Viable (PMV). La culminación de este esfuerzo es una API alojada en la nube que realiza dos funciones clave de Machine Learning. En primer lugar, realiza un análisis de sentimientos sobre los comentarios de los usuarios, proporcionando valiosos insights sobre la experiencia del usuario. En segundo lugar, desarrolla un sistema de recomendación de juegos que opera tanto a partir del nombre de un juego como de las preferencias específicas de un usuario. Este proyecto ilustra mi capacidad para realizar diversas operaciones de MLOps, desde la transformación de datos hasta la implementación y optimización de la carga de datos. En resumen, este trabajo individual simula el rol combinado de Data Engineer y Data Scientist para ofrecer soluciones avanzadas en la plataforma de juegos Steam. </p>

<hr></p>

# DATOS
Este proyecto se basó en el análisis de tres archivos JSON fundamentales: 

- <b>"Australian_user_reviews.json":</b> abarca las opiniones de los usuarios sobre los juegos, incluyendo recomendaciones, emoticones de humor, estadísticas de utilidad del comentario, y datos cruciales como el ID del usuario y del juego comentado. </p>

- <b>"Australian_users_items.json":</b> " ofrece una visión detallada de los más jugados por cada usuario, junto con el tiempo acumulado dedicado a cada título, proporcionando una perspectiva valiosa sobre las preferencias individuales de los jugadores. </p>


- <b> "Output_steam_games.json":</b>  engloba información fundamental sobre los juegos en sí, desde títulos y desarrolladores hasta precios, características técnicas y etiquetas, creando un catálogo completo de juegos disponibles en la plataforma. </p>

<hr></p>


# TAREAS DESARROLLADAS



## TRANSFORMACIONES  </p>

<p style="text-align: justify;">  El proceso de Extracción, Transformación y Carga (ETL) de los tres conjuntos de datos proporcionados fue un componente esencial en la preparación de la información para el desarrollo del proyecto. Enfrentando la complejidad de archivos JSON, se aplicaron estrategias específicas para desanidar columnas y transformar datos anidados en estructuras más accesibles.

<p style="text-align: justify;"> Durante la fase de transformación, se abordaron desafíos como la presencia de filas completas con valores nulos, lo que requería medidas para mantener la integridad de los datos restantes. La tarea también incluyó el llenado de campos vacíos para asegurar la completitud de variables esenciales. Con el objetivo de optimizar el rendimiento de la API y considerando restricciones de almacenamiento en el despliegue, se adoptó una estrategia de eliminación de columnas insignificantes o con valores nulos significativos, basada en una evaluación cuidadosa de su contribución al proyecto.

<p style="text-align: justify;"> El proceso completo, documentado en archivos específicos para cada conjunto de datos, implicó el uso de la biblioteca Pandas en un entorno de Visual Studio Code (VSCode) con Jupyter Notebook, respaldado por Python y las bibliotecas numpy. Este enfoque permitió una manipulación eficiente y transformación de datos para obtener un conjunto limpio y optimizado. La fase de ETL también incorporó pasos cruciales, como la eliminación de duplicados, el filtrado de fechas inválidas y la creación de nuevas columnas para mejorar la eficiencia de la API. La gestión cuidadosa de valores nulos y la identificación de outliers aseguraron la calidad y coherencia de los datos, preparándolos de manera óptima para el análisis y la implementación en la API desarrollada. Este proceso demuestra un enfoque meticuloso para garantizar la calidad y utilidad de los datos en todo el proyecto. </p>




## FEATURE ENGINEERING </p>

<p style="text-align: justify;">Para mejorar la comprensión y evaluación del sentimiento asociado a las reseñas de usuarios en el conjunto de datos "user_reviews", se implementó un análisis de sentimiento mediante la incorporación de una nueva columna denominada 'sentiment_analysis'. Se utilizó la biblioteca de procesamiento de lenguaje natural (NLP) TextBlob para calcular la polaridad de sentimiento de cada revisión y asignar valores numéricos en función de su tono emocional.

<p style="text-align: justify;"> Se estableció una escala de tres categorías: '0' para reseñas con sentimiento negativo, '1' para reseñas neutrales, y '2' para reseñas con sentimiento positivo. Los umbrales de polaridad se definieron en -0.5 y 0.5, clasificando las reseñas como negativas por debajo de -0.5, positivas por encima de 0.5, y neutrales en el rango intermedio.Este enfoque ofrece una evaluación más detallada del sentimiento expresado en las reseñas, proporcionando información cuantitativa sobre la percepción de los usuarios hacia los juegos. </p>


## ANALISIS EXPLORATORIO DE LOS DATOS EDA

<p style="text-align: justify;"> En el proceso de Análisis Exploratorio de Datos (EDA), se priorizó la identificación de variables clave para la construcción del modelo de recomendación y las funciones. Durante este examen minucioso, se enfocó en variables cruciales para comprender los patrones de comportamiento y preferencias de los usuarios. Además, se exploraron otras variables de manera amplia para evaluar su posible impacto en el modelo. Este enfoque exhaustivo proporcionó una comprensión integral del conjunto de datos, destacando no solo las variables críticas para el modelo, sino también aquellas que podrían ofrecer información valiosa sobre diversos aspectos. El EDA abarcó los tres conjuntos de datos sometidos a ETL, utilizando Pandas para la manipulación de datos y las librerías Matplotlib y Seaborn para la visualización.  </p>


## MODELO

<p style="text-align: justify;"> La medida de similitud del coseno fue fundamental en la construcción del modelo de recomendación. Esta métrica, comúnmente empleada para evaluar la similitud entre vectores en un espacio multidimensional, se aplicó para determinar la similitud entre juegos en el enfoque ítem-ítem. Este análisis se centró en variables clave como género e item_name. Se seleccionó un juego de referencia, y la recomendación se fundamentó en qué tan cercanos eran los demás juegos en términos de estas características específicas. La similitud del coseno proporcionó una evaluación precisa de la afinidad entre los elementos, contribuyendo así a la generación de recomendaciones significativas en el contexto del modelo de recomendación.  </p>

<hr></p>

# DESARROLLO API

Para el desarrollo de la API, se optó por utilizar el framework FastAPI, implementando diversas funciones para consultas específicas. Estas funciones incluyen:

- <p style="text-align: justify;"><b>PlayTimeGenre:</b>  Proporciona el año con la mayor cantidad de horas jugadas para un género específico.

- <p style="text-align: justify;"><b>UserForGenre:</b> Retorna el usuario que acumula la mayor cantidad de horas jugadas para el género especificado. Además, ofrece una lista detallada de la acumulación de horas jugadas por año.

- <p style="text-align: justify;"><b>UsersRecommend:</b>  Devuelve el top 3 de juegos más recomendados por usuarios para el año especificado, considerando revisiones marcadas como recomendadas y comentarios positivos o neutrales

- <p style="text-align: justify;"><b>UsersWorstDeveloper:</b> Proporciona el top 3 de desarrolladoras con juegos menos recomendados por usuarios para el año dado. Solo se consideran juegos con revisiones marcadas como no recomendadas y comentarios negativos.

- <p style="text-align: justify;"><b>Sentiment_analysis:</b>  Realiza un análisis de sentimiento según la empresa desarrolladora, ofreciendo un diccionario con el nombre de la desarrolladora como clave y una lista que detalla la cantidad total de registros de reseñas categorizados con un análisis de sentimiento.

- <p style="text-align: justify;"><b>Recomendacion_juego:</b> Diseñada para un sistema de recomendación ítem-ítem, devuelve una lista con 5 juegos recomendados similares al producto ingresado. 

<p style="text-align: justify;"> Es esencial destacar que todas estas funciones fueron implementadas y desplegadas en un entorno virtual de FastAPI, optimizando su rendimiento en la plataforma Render mediante la generación de dataframes más pequeños sin comprometer la calidad de la información ofrecida.


El desarrollo de las funciones de consultas generales se puede ver en [Funciones](https://github.com/AylinRengifo/Proyecto-Individual-1/blob/main/Jupyters/5.%20Funciones.ipynb). El desarrollo del código para las funciones del modelo de recomendación se puede ver en [Modelo](https://github.com/AylinRengifo/Proyecto-Individual-1/blob/main/Jupyters/6.%20Modelo.ipynb). Pueden encontrar el Deploy en Render/FastAPI en  [API] (https://proyecto-individual-08oa.onrender.com)


<hr></p>


# CONCLUSIONES

<p style="text-align: justify;">  Durante el desarrollo de este proyecto, se realizaron diversas tareas fundamentales que abarcaron desde la extracción y transformación de datos hasta la implementación de funciones en una API y la creación de modelos de recomendación. Se exploraron conjuntos de datos detallados que abordaban aspectos clave de la plataforma Steam, incluyendo reseñas de usuarios, información de juegos y datos de usuarios.

<p style="text-align: justify;">  El proceso ETL (Extracción, Transformación y Carga) permitió gestionar archivos JSON, desanidar datos anidados y abordar valores nulos, garantizando la integridad y eficiencia de los conjuntos de datos resultantes. Se aplicaron estrategias específicas para adaptar la información a las necesidades del proyecto, y se llevaron a cabo análisis exploratorios y de sentimiento para comprender mejor la dinámica de la plataforma y las preferencias de los usuarios. La creación de una API con FastAPI y la implementación de funciones específicas, como consultas de usuarios, análisis de géneros y recomendaciones de juegos, proporcionaron una interfaz de usuario amigable y accesible para interactuar con los datos analizados.

<p style="text-align: justify;">  Además, se abordaron desafíos específicos, como la limitación de capacidad de almacenamiento en el despliegue de la API en la plataforma Render. Se tomaron decisiones clave, como la optimización de consultas y la generación de dataframes más pequeños para mejorar el rendimiento en este entorno. Para finalizar se pueden resaltar áreas de mejora y desarrollo continuo. La calidad de los datos, la actualización temporal, y la exploración de alternativas para el despliegue representan oportunidades significativas. 

o.



# TECNOLOGIAS USADAS

![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
