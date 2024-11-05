from pydantic import BaseModel

class cliente(BaseModel):
    documento:str
    nombre:str
    apellido:str
    correo:str
    celular:str
    edad:int