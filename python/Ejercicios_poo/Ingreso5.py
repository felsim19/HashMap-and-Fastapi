#Diseña una clase `Tarea` para representar una tarea por hacer. Permite agregar nuevas tareas, marcarlas como completadas y listar las tareas pendientes.
from ejercicio5 import tarea
manejotareas = tarea()
while(True):
    op = int(input("1.agregar tareas\n2.completar tareas\n3.Mostrar tareas\n4.salir\n"))
    if (op == 1):
        tareas = str(input("Agrege la nueva tarea "))
        manejotareas.agregar_tareas(tareas)
    elif(op == 2):
        completado = str(input("cual tarea ya ha completado? "))
        manejotareas.completar_tareas(completado)
    elif(op == 3):
        manejotareas.listar_pendientes()
    elif(op == 4):
        print("adios")
        break
    
        