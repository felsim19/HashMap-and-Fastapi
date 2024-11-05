diccionario = {'Felipe': (48+50+45)/3,
               'mateo': (45+36+38)/3,
               'ferxxo': (45+39+38)/3,
               'david' : (45+46+32)/3,
               'juan' : (45+39+32)/3,
               }
print(diccionario.items())
def devolver(diccionario):
    NumeroMayor = 0
    estudianteM = ''
    for nombre, nota in diccionario.items():
        if nota > NumeroMayor:
            NumeroMayor = nota
            estudianteM = nombre
    return NumeroMayor, estudianteM
mayor,estudiante = devolver(diccionario)
print(f"El mayor promedio es de {mayor} y es del estudiante {estudiante}")



