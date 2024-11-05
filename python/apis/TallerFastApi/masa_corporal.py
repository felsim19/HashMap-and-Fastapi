from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Exerciese one": "Desarrolla un servicio que reciba el peso (en kilogramos) y la altura (en metros) de una persona como parámetros en la URL y devuelva su IMC"}

@app.get("/{peso}/{altura}")
async def CalcularIMC(peso:int,altura:float):
    alturaCuadada = altura*altura
    imc = peso/alturaCuadada
    return {f"Your IMC is": imc}