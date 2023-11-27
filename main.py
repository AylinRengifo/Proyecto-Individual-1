from fastapi import FastAPI
import pandas as pd
import json
import numpy as np
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from fastapi.responses import HTMLResponse


# Se instancia la aplicación
app = FastAPI()




#Carga los datos parquet en un dataframe de pandas
Tabla_API = pd.read_parquet('Tabla_API.parquet')
funcion3= pd.read_parquet('funcion3.parquet')
funcion4= pd.read_parquet('funcion4.parquet')
funcion5= pd.read_parquet('funcion5.parquet')
recomendaciones= pd.read_parquet('recomendaciones.parquet')



@app.get(path="/", response_class=HTMLResponse, tags=["Homepage"])
def hola():
    return ''' 
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proyecto  Individual Steam API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            padding: 20px;
        }
        h1 {
            color: #0366d6; /* Azul de Steam */
            text-align: center;
        }
        p {
            color: #333;
            font-size: 18px;
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Proyecto Steam API</h1>
    <p>Bienvenido a la API del proyecto relacionado con Steam. Aquí puedes acceder a información emocionante sobre juegos, usuarios y más. 

    <p>¡Explora la API para descubrir más funcionalidades emocionantes! Se puede ver el funcionamiento de esta si se coloca /docs en la barra de busqueda</p>

    </p>

    <footer>
        <p>© 2023 Proyecto Steam API. Aylin Lizett Rengifo Gutierrez</p>
    </footer>
</body>
</html>

    ''' 



    #Funciones 
 


#Funcion 1


@app.get(path='/PlayTimeGenre',           
         description = """ <font color="darkblue">
                         DESCRIPCION <br>
                         Al ingresar un genero devuelve el año con mas horas jugadas para este
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el genero en la caja de texto inferior. Ejemplo de generos: Action,Adventure, Casual, Indie, Simulation,entre otros<br>
                        3. Bajar a "Resposes"  para devolver año con más horas jugadas para dicho género. 
                        </font>
                        """,
         tags=["Features"])

def PlayTimeGenre(genero: str):
    # Filtrar el DataFrame por el género específico
  genero_data = Tabla_API[Tabla_API['genres'].str.contains(genero, case=False, na=False)]

  # Verificar si se encontraron datos para el género especificado
  if genero_data.empty:
      print(f"No hay datos para el género {genero}.")
      return None

  # Encontrar el año con más horas jugadas
  max_hours_row = genero_data.groupby('year_release')['playtime_forever'].sum().idxmax()

  # Imprimir el resultado
  result = f"El año con más horas jugadas para el género {genero}: {max_hours_row}"
  return result




#Funcion 2

@app.get('/UserForGenre', 
         description = """ <font color="darkblue">
                         DESCRIPCION <br>
                         Al ingresar un genero devuelve el usuario que acumula mas horas jugadas para el genero dado y un alista de la acumulacion de horas jugadas por año.
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el genero en la caja de texto inferior. Ejemplo de generos: Action,Adventure, Casual, Indie, Simulation,entre otros<br>
                        3. Bajar a "Resposes"  para ver el usuario con más horas jugadas para el genero dado y descripción por año.
                        </font>
                        """,
          tags=["Features"])

def UserForGenre(genre):
   # Filtrar el DataFrame por el género específico
   genre_data = Tabla_API[Tabla_API['genres'].str.contains(genre, case=False, na=False)]

   # Verificar si se encontraron datos para el género especificado
   if genre_data.empty:
       print(f"No hay datos para el género {genre}.")
       return None

   # Agrupar por usuario y sumar las horas jugadas
   user_playtimes = genre_data.groupby('user_id')['playtime_forever'].sum()

   # Encontrar el usuario con más horas jugadas
   user_max_playtime = user_playtimes.idxmax()

   # Obtener la acumulación de horas jugadas por año
   playtime_by_year = genre_data.groupby('year_release')['playtime_forever'].sum().reset_index()

   # Crear un diccionario con los resultados
   result = {
       'Usuario_con_mas_horas_jugadas': user_max_playtime,
       'Horas_jugadas_por_año': playtime_by_year.to_dict('records')
   }
   return result
   
   
#Funcion 3

@app.get('/UsersRecommend', 
         description = """ <font color="darkblue">
                        DESCRIPCION <br>
                         Al ingresar un año devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el año en la caja de texto inferior. Ejemplo de generos: Action,Adventure, Casual, Indie, Simulation,entre otros<br>
                        3. Bajar a "Resposes"  para ver el top 3 de juegos MÁS recomendados.
                        </font>
                        """,
          tags=["Features"])

def UsersRecommend(year: int) :
 # Filtrar el DataFrame por el año específico y las recomendaciones positivas o neutrales
 year_data = funcion3[(funcion3['year_review'] == year)]
 year_data1 = funcion3[(funcion3['recommend'] == True) & (funcion3['sentiment_analysis'].isin([2, 1]))]
 year = year_data1.groupby('item_name')['recommend'].sum().sort_values(ascending=False).head(3)
 result = pd.DataFrame(year).to_dict()
 # Convertir el resultado a una lista de diccionarios
 result = [{"Puesto " + str(i+1) : v} for i, v in enumerate(result['recommend'])]

 return result



#Funcion 4


@app.get('/UsersWorstDeveloper/', 
         description = """ <font color="darkblue">
                        DESCRIPCION <br>
                         Al ingresar un año devuelve el top 3 de desarrolladoras con juegos MENOS recomendados por usuarios para el año dado.
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el año en la caja de texto inferior. Ejemplo de generos: Action,Adventure, Casual, Indie, Simulation,entre otros<br>
                        3. Bajar a "Resposes"  para ver el top 3 de desarrolladoras MÁS recomendadas.
                        </font>
                        """,
          tags=["Features"])


def UsersWorstDeveloper(year: int):
 # Filtrar el DataFrame por el año específico y las recomendaciones positivas o neutrales
 year_data = funcion4[(funcion4['year_review'] == year)]
 year_data1 = funcion4[(funcion4['recommend'] == False) & (funcion4['sentiment_analysis']== 0)]
 year= year_data1.groupby('developer')['recommend'].sum().sort_values(ascending=False).head(3)
 result = pd.DataFrame(year).to_dict()
 # Convertir el resultado a una lista de diccionarios
 result = [{"Puesto " + str(i+1) : v} for i, v in enumerate(result['recommend'])]

 return result




#Funcion 5

@app.get('/sentiment_analysis/', 
         description = """ <font color="darkblue">
                        DESCRIPCION <br>
                         Al ingresar una desarrolladora devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor.
                        INSTRUCCIONES<br>
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese la desarrolladora  en la caja de texto inferior. Ejemplo de generos: Action,Adventure, Casual, Indie, Simulation,entre otros<br>
                        3. Bajar a "Resposes"  para el analisis de sentimientos.

                        </font>
                        """,
          tags=["Features"])

def sentiment_analysis(empresa_desarrolladora: str) -> dict:
  # Crear un diccionario que mapee los valores '0', '1' y '2' a 'Negativo', 'Neutral' y 'Positivo'
  sentiment_mapping = {0: 'Negativo', 1: 'Neutral', 2: 'Positivo'}
  # Reemplazar los valores en la columna 'sentiment_analysis'
  funcion5['sentiment_analysis'] = funcion5['sentiment_analysis'].replace(sentiment_mapping)
  # Filtrar el DataFrame por la empresa desarrolladora
  df_filtered = funcion5[funcion5['developer'] == empresa_desarrolladora]
  # Verificar si se encontraron datos para la empresa desarrolladora
  if df_filtered.empty:
      print(f"No hay datos para la empresa {empresa_desarrolladora}.")
      return None
  # Agrupar por análisis de sentimiento y contar las filas
  df_grouped = df_filtered.groupby(['developer', 'sentiment_analysis']).size().reset_index(name='Numero de registros')
  # Convertir el DataFrame agrupado en un diccionario con el nombre de la empresa desarrolladora como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor
  sentiment_analysis = {empresa_desarrolladora: df_grouped.set_index('sentiment_analysis')['Numero de registros'].to_dict()}

  return sentiment_analysis



# Modelo de Recomendacion


@app.get("/recomendacion_juego/{id_producto}", 
         description = """ <font color="darkblue">
                        DESCRIPCION <br>
                         Devuelve 5 recomendaciones de juegos similares a uno del que ponemos su id.
                        1. Haga clik en "Try it out".<br>
                        2. Ingrese el id del juego en la caja de texto inferior. Ejemplo de generos: Action,Adventure, Casual, Indie, Simulation,entre otros<br>
                        3. Bajar a "Resposes"  para el analisis de sentimientos.
                        
                        </font>
                        """,
          tags=["Features"])



def recomendacion_juego(id_producto: int):
    recomendacion = recomendaciones[recomendaciones['item_id'] == id_producto]['recomendaciones'].iloc[0]
    # Verificar si la lista de recomendaciones tiene valores
    if len(recomendacion) > 0:
        recomendaciones_dict = {i + 1: juego for i, juego in enumerate(recomendacion)}
        return recomendaciones_dict
    else:
        # Si no se encuentra, devolver una respuesta JSON con el código de estado 404
        error = {'detail': 'No se encontraron recomendaciones para el ID proporcionado'}
        
        return JSONResponse(content=error, status_code=404)






