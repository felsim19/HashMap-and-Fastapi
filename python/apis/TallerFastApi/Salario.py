from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Exercise six":"Camilo, un empleado de una compañía de desarrollo software tiene dudas sobre silos pagos que le realiza la empresa de manera mensual son correctos"}

@app.get("/{salario_base}/{horas_extras}")
async def Calcular(salario_base:float, horas_extras:int):
    hora_normal = float(salario_base/192)
    valorExtra = hora_normal*1.25
    totalextra = (valorExtra * horas_extras)
    bonificacion = salario_base*0.05
    subsalario = salario_base + totalextra + bonificacion
    descuento_salud = subsalario*0.03
    descuento_prension = subsalario*0.4
    descuento_caja = subsalario*0.1
    descuento_total = (descuento_caja + descuento_prension + descuento_salud) 
    SalarioTotal = subsalario - descuento_total
    return {"Estimado empleado su salario total es de": f"sub salario {subsalario} totaldescuento {descuento_total} salariototal {SalarioTotal}"}