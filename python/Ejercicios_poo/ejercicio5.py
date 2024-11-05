class tarea:
    def __init__(self):
        self.lista = []
        self.listaCompletada = []
    
    def agregar_tareas(self, tarea):
        self.lista.append(tarea)
        
    def completar_tareas(self, completado):
        if (completado in self.lista):
            self.lista.remove(completado)
            print("esta tarea se acabo de completar")   
        else:
            print("Esa tarea no estaba en la lista")
        
    def listar_pendientes(self):
        print("Las tareas pendientes son : ")
        for i in self.lista:
            print(i)
        