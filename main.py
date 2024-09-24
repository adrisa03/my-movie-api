from fastapi import FastAPI #importa la clase fastapi de la libreria fastapi

app = FastAPI() #crea una instancia de la clase fastapi
app.title = 'Mi primer aplicacion de peliculas y analisis de datos'
app.version = '0.0.1' #asigna un valor a la propiedad title de la clase fastapi
@app.get('/', tags=['Home']) #definiendo una ruta
def message(): #definiendo una funcion de la ruta
    return 'Hello World' #devolviendo un valor
