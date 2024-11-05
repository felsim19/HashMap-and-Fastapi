from pydantic import BaseModel

class Producto(BaseModel):
    Id: int
    Nombre: str
    Precio: str
    Cantidad: int
    