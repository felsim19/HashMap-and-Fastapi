class Contacto:
    def __init__(self, nombre, telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        
    def ObtenerNombre(self):
        return self.nombre
