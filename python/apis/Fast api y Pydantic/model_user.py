from pydantic import BaseModel

class Usuario(BaseModel):
    Id: int
    Nombre: str
    Email: str
    Edad: int