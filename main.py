from fastapi import FastAPI 
from fastapi import FastAPI,Query # Importamos la libreria FastAPI
from fastapi.responses import JSONResponse # Importamos la libreria JSONResponse
from fastapi.responses import HTMLResponse
from typing import Optional
import nltk # Importamos la libreria Optional para volver parametros opcionales

app = FastAPI() #Crea una instancia de la clase FastAPI 
app.title = "App Diez mejores películas de los ultimos 10 años con FastAPI"
app.version = "0.0.1"

movies_list = [
     {
        "id": 1,
        "title": "12 Years a Slave",
        "overview": "Película dramática de Steve McQueen",
        "year": 2013,
        "rating": 8.0,
        "category": "Drama"
    },
    {
        "id": 2,
        "title": "La inesperada virtud de la ignorancia",
        "overview": "Riggan Thomson (Michael Keaton) es un actor en declive conocido por interpretar al superhéroe Birdman",
        "year": 2014,
        "rating": 7.9,
        "category": "Teatro"
    },
    {
        "id": 3,
        "title": "En primera plana",
        "overview": "Drama estadounidense",
        "year": 2015,
        "rating": 8.0,
        "category": "Drama"
    },
    {
        "id": 4,
        "title": "Luz de Luna",
        "overview": "Drama basado en la obra semi-autobiográfica de Tarell Alvin McCraney",
        "year": 2016,
        "rating": 8.5,
        "category": "Drama"
    },
    {
        "id": 5,
        "title": "La forma del agua",
        "overview": "Una obra cumbre de Guillermo del Toro",
        "year": 2017,
        "rating": 8.1,
        "category": "Fantasia"
    },
    {
        "id": 6,
        "title": "Green Book una amistad sin fronteras",
        "overview": "Inspirada en una historia real",
        "year": 2018,
        "rating": 7.8,
        "category": "Historia"
    },
    {
        "id": 7,
        "title": "Parasitos",
        "overview": "Película surcoreana dirigida por Bong Joon-ho",
        "year": 2019,
        "rating": 8.0,
        "category": "Humor y suspenso"
    },
    {
        "id": 8,
        "title": "Nomadland",
        "overview": "El largometraje sigue a Fern (Frances McDormand)",
        "year": 2020,
        "rating": 7.0,
        "category": "Ficcion"
    },
    {
        "id": 9,
        "title": "CODA Señales del corazon",
        "overview": "Este filme de Sian Heder está protagonizado por una joven llamada Ruby (Emilia Jones)",
        "year": 2021,
        "rating": 8.0,
        "category": "Drama"
    },
    {
        "id": 10,
        "title": "Todo en todas partes al mismo tiempo",
        "overview": "Es una pelicula audaz que rompe moldes",
        "year": 2022,
        "rating": 8.0,
        "category": "Ficcion"
    }
]

@app.get('/', tags=["Home"])#Definimos una ruta
def message(): # Definimos una función de la ruta
    return HTMLResponse ('<h1>Hello world I´m Luis Fernando Meneses</h1>') # Devolvemos un string en la respuesta de la ruta

@app.get('/Peliculas', tags=["Peliculas"])#Definimos una ruta de la clase FastAPI
def get_movies(): 
    return movies_list

@app.get('/Peliculas/{id}', tags=["Peliculas"])#Definimos una ruta de la clase FastAPI
def get_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            return item
    return []

#Tokenizar
@app.post("/Tokenizar") # Decorador para indicar que es una ruta de la API
def tokenize(text:str): # Funcion que retorna un mensaje
    return preprocessar(text)

def preprocessar(text):
    import json  # Importamos la librería json para trabajar con archivos json
    from nltk.tokenize import word_tokenize
    import nltk
    nltk.download('punkt')
    tokens = word_tokenize(text)
    result = {word: True for word in tokens}
    print(result)
    return JSONResponse(content={"message":result})
    