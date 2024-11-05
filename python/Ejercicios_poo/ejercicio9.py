class Paquete:
    numeroserie = 0
    def __init__(self, origen, destino):
        self.numeroserie += 1
        self.origen = origen
        self.destino = destino
        self.estado = "Preparacion"
        
    def EditarEstado(self, estadoNuevo):
        self.estado = estadoNuevo
        
    def ConsultarUbicacion(self):
        return self.estado
    
    def __str__(self):
        return(f"Paquete {self.numeroserie}:\n"
               f"Origen: {self.origen}\n"
               f"Destino: {self.destino}\n"
               f"Estado actual: {self.estado}\n")