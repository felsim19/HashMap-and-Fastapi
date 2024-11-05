from ejericicio10 import Contacto

class ManejoContacto:
    
    def __init__(self):
        self.lista = []
        
    def AgregarContacto(self,nombre,telefono,correo):
        Usuario = Contacto(nombre,telefono,correo)
        self.lista.append(Usuario)
        
    def MostarLista(self):
        if not self.lista:
            print("No hay nada dentro de la lista")
        else:
            for contacto in self.lista:
                print(f"Nombre : {contacto.nombre}\n"
                      f"Telefono : {contacto.telefono}\n"
                      f"Correo : {contacto.correo}")    
    
    def ConsultarNombre(self, nombre):
        if not self.lista:
            print("No hay nada dentro de la lista")
        else:
            for contacto in self.lista:
                if contacto.nombre == nombre:
                    print("El ")