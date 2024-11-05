from fastapi import FastAPI
from bd import baseDatos

app = FastAPI()

usuarios = {}
usuarios = baseDatos()


@app.get("/")
async def root():
    return usuarios

@app.get("/cliente/{id}")
async def consultar(id:str):
    for valor in usuarios.values():
        if valor["documento"]==id:
            return valor