from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Exerciese two": "Crea un servicio que reciba la cantidad a convertir y las monedas de origen y destino como parámetros en la URL, y devuelva la cantidad convertida"}

@app.get("/{cantidad}/{monedas_origen}/{monedas_destino}")
async def ConvertirMonedas(cantidad: float, monedas_origen: float, monedas_destino: float):
    cantidad_base = cantidad / monedas_origen
    cantidad_total = round(cantidad_base * monedas_destino,2)
    return {"Su conversion de monedas es":cantidad_total}