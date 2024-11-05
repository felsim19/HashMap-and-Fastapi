from pydantic import BaseModel

class Cliente(BaseModel):
    Apellido: str
    Celular: str
    Correo: str
    Documento: str
    Nombre:str