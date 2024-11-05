from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Exercise three":" Cálculo del Tiempo de Viaje: Implementa un algoritmo que reciba la distancia a recorrer (en kilómetros) y la velocidad media (en kilómetros por hora) como parámetros en la URL, y calcule el tiempo estimado de viaje."}

@app.get("/{distancia}/{velocidad_media}")
async def Calculartiempo(distancia:int,velocidad_media:int):
    Despejar = distancia/velocidad_media
    return{"Su tiempo de viaje fue de":f"{Despejar} horas"}