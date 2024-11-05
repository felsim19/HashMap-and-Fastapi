from fastapi import FastAPI, HTTPException
from model import cliente
import json


app = FastAPI()

with open('datos.json', 'r')as txt:
    datoscliente = json.load(txt)
    listaclientes = [cliente(**i)for i in datoscliente]
    
@app.get("/cliente")
async def Consultar():
    return listaclientes

@app.get("/cliente/{documento}")
async def consultarCliente(documento:str):
    for c in listaclientes:
        if c.documento == documento:
            return c
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.post("/cliente", response_model=cliente)
async def Insertar(cliente:cliente):
    for c in listaclientes:
        if c.documento == cliente.documento:
            raise HTTPException(status_code=404, detail="El usuario ya existe")
     
    listaclientes.append(cliente) 
    
    with open("datos.json","w")as txt:
        json.dump([c.dict() for c in listaclientes], txt, indent=4)
    return c


@app.put("/cliente/{documento}",response_model=cliente)
async def Actualizar(documento:str, clienteAcutualizado:cliente):
    for i, datos in enumerate(listaclientes):
        if datos.documento == documento:
            listaclientes[i] = clienteAcutualizado
            with open("datos.json","w")as txt:
                json.dump([j.dict() for j in listaclientes], txt, indent=4)
                return clienteAcutualizado
    raise HTTPException(status_code=404, detail="El documento ya existe")

@app.delete("/cliente/{documento}")
async def eliminarCliente(documento:str):
    for c in listaclientes:
        if c.documento == documento:
            listaclientes.remove(c)
            with open("datos.json","w")as txt:
                json.dump([j.dict() for j in listaclientes], txt, indent=4)
    raise HTTPException(status_code=200 , detail="El documento se borro")
    
    