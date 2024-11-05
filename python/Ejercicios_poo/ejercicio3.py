class Estudiante:
    def __init__(self,Nombre,edad,calificaiones):
        self.nombre = Nombre
        self.edad = edad
        self.calificaiones = calificaiones

    def ObtenerNombre(self):
        return self.nombre
    
    def ObtenerEdad(self):
        return self.edad
    
    def ObtenerCalifiaciones(self):
        return self.calificaiones
    
    def promedio(self):
        lista = self.ObtenerCalifiaciones()
        promedio = 0
        for i in lista:
            promedio += i
        total = promedio/len(lista)
        return total
    
    def to_string(self):
        mensaje = f"Su nombre es {self.ObtenerNombre()} y su edad es {self.ObtenerEdad()} y su promedio es de {self.promedio()}"
        return mensaje