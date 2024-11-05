materias = []
estudiantes = []
cantidad = int(input("Digite la cantidad de materias que va a dictar "))
for i in range(cantidad):
    mat = str(input("Digite la materia "))
    materias.append(mat)
    cat = int(input("Digite la cantidad de estudiante que va a tener esta materia "))
    lista = []
    for j in range(cat):
        nom = str(input("Digite el nombre del estudiante "))
        lista.append(nom)
    estudiantes.append(lista)
print(estudiantes)
def agrupar(materias,estudiantes):
    diccionario = {}
    for i in range(len(materias)):
        diccionario[materias[i]] = estudiantes[i]
    return diccionario
print(agrupar(materias,estudiantes))


palabras = []
cantidad = int(input("Digite la cantidad de palabras que va a añadir "))
for i in range(cantidad):
    word = str(input("Ingrese las palabras "))
    palabras.append(word)
print(palabras)
def palabrasLongitud(lista):
    nuevalista = []
    for i in range(len(lista)):
        palabra_mayor = ""
        longitud_mayor = 0
        for x in lista:
            if len(x) > longitud_mayor:
                longitud_mayor = len(x)
                palabra_mayor = x
        nuevalista.append(palabra_mayor)
        nuevalista.append(longitud_mayor)
        lista.remove(palabra_mayor)
    return nuevalista
print(palabrasLongitud(palabras))

