from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"Exercise four":"Desarrolla un servicio que reciba la longitud deseada de la contraseña como parámetro en la URL y genere una contraseña aleatoria de esa longitud."}

@app.get("/{longitud}")
async def generarcontraseña(longitud:int):
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVXYZ"
    abcminus = abc.lower()
    numeros = "0123456789"
    letras = abc + abcminus + numeros
    palabra = ""
    for i in range(longitud):
        numero = random.randint(0,len(letras) -1)
        letra = letras[numero]
        palabra += str(letra)
    return {"La contraseña aleatoria es": palabra}