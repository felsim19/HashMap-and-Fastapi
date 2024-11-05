class Estudiante:

    def __init__(self, documento, nombre, apellido, correo, celular, edad) :
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.celular = celular
        self.edad = edad

    def obtenerdocumento(self):
        return self.documento
    
    def obtenernombre(self):
        return self.nombre
    
    def obtenerapellido(self):
        return self.apellido
    
    def obtenercorreo(self):
        return self.correo
    
    def obtenercelular(self):
        return self.celular
    
    def obteneredad(self):
        if self.edad>=18:
            mensaje = "Es mayor de edad"
        else:
            mensaje = "Es menor de edad"
        return self.edad, mensaje