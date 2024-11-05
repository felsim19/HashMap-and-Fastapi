from pydantic import BaseModel

class Orden(BaseModel):
    ID:int
    IDUSERS:int
    Lista_productos: list[int]
    total : float = 0.0
    
    def calcularTotal(cls,productos,id_productos):
        total = 0.0
        for producto in productos:
            if producto['Id'] in id_productos:
                price = float(producto[('Precio')])
                total += price
        return total