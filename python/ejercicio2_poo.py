class User:
    def __init__(self, nombre, correo, usuario, contraseña) :
        self.nombre = nombre
        self.correo = correo
        self.usuario = usuario
        self.contraseña = contraseña

    def obtenerNombre(self):
        return self.usuario
    
    def obtenerusuario(self):
        return self.usuario

    def obtenerContraseña(self):
        return self.contraseña
    
    def ValidarContraseña(self, contraseña):
        if contraseña == self.contraseña:
            return True
        else:
            return False