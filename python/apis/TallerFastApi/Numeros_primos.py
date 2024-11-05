from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Exercise five":"Crea un servicio que reciba un rango de números (inicio y fin) como parámetros en la URL y devuelva una lista de los números primos dentro de ese rango."}

@app.get("/{numeroinicial}/{numerofinal}")
async def NumerosPrimos(numeroinicial:int,numerofinal:int):
    primos = []
    for i in range(numeroinicial,numerofinal + 1):
        if i < 2:
            es_primo = False
        else:
            es_primo = True
            for x in range(2, int(i**0.5) + 1):
                if i % x == 0:
                    es_primo = False
                    break
        if es_primo:
            primos.append(i)
    return{"Los numeros primos entre los rangos dados son": primos}
    