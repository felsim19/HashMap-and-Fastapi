class Vuelo:
    def __init__(self, origen,destino,numero_asientos_disponibles):
        self.origen = origen
        self.destino = destino
        self.numero_asientos_disponibles = numero_asientos_disponibles  
    
    def reservar_asientos(self, asientos):
        if (self.numero_asientos_disponibles - asientos < 0):
            print("Numero de asientos nos disponibles")
        else:
            self.numero_asientos_disponibles -= asientos
            print("Asientos comprados")
    
    def consultar_asientos(self):
        return print(f"La cantidad de asientos disponibles es de {self.numero_asientos_disponibles}")