from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return{"Exercise seven":"Usted hace parte del equipo de desarrollo encargado de construir el software que procesará los datos registrados por las cámaras. Su misión es crear un programa en Python que permita saber si un conductor debe ser multado o no."}

@app.get("/{Radares}/{TiempoMinutos}/{VelocidadPermitida}")
async def Calcular(Radares:int,TiempoMinutos:int,VelocidadPermitida:int):
    distanciaCamara = Radares
    tiempoSegundos = (TiempoMinutos * 60)
    tiempoHoras = (tiempoSegundos/3600)
    velocidadFinal = distanciaCamara/tiempoHoras
    if(velocidadFinal > VelocidadPermitida):
        return{f"Su velocidad maxima fue de {velocidadFinal} km y esta en una zona de {VelocidadPermitida} km": f"Por lo tanto usted llevara una multa por exceso de velocidad"}
    else:
        return{f"Su velocidad maxima fue de {velocidadFinal} km y esta en una zona de {VelocidadPermitida} km": f"Por lo tanto usted no sera multado"}