from fastapi import FastAPI #importa la clase fastapi de la libreria fastapi
from fastapi.responses import HTMLResponse #importa la clase HTMLResponse de la libreria fastapi
from movies_list import movies_list
app = FastAPI() #crea una instancia de la clase fastapi
app.title = 'Mi primer aplicacion de peliculas y analisis de datos'
app.version = '0.0.1' #asigna un valor a la propiedad title de la clase fastapi
@app.get('/', tags=['Home']) #definiendo una ruta
def message(): #definiendo una funcion de la ruta
    return HTMLResponse('<h1>Hello World</h1>') #retorna un objeto de la clase HTMLResponse
    
@app.get('/movies', tags=['Movies']) #definiendo una ruta de la clase fast api
def movies(): #definiendo una ruta
    return movies_list

@app.get('/movies/{id}', tags=['Movies']) #app get consultar por id
def get_movie(id:int): #
    for item in movies_list:
        if item['id'] == id:
            return item
    return []