def listaPrincipal():
    listaPrincipal = []
    cantidad = int(input("Cuantas sublista va a tener la lista"))
    for i in range(cantidad):
        suublista = []
        cantidad = int(input("cuantos datos va a tener esta sublista?"))
        for x in range(cantidad):
            palabras = str(input("Ingrese las palabras "))
            suublista.append(palabras)
        listaPrincipal.append(suublista)
    return listaPrincipal
print(listaPrincipal())