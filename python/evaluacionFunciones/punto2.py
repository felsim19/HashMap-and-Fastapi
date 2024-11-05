cantidad = int(input("Bienvenido ingrese la cantidad de palabras que va a ingresar a la lista "))
nombres = []
for p in range(cantidad):
    nombre = str(input("Ingrese el nombre "))
    nombres.append(nombre)
print(nombres)
def convertir(lista):
    diccionario = {}
    for i in nombres:
        PrimeraLetra = i[0]
        sublista = []
        print(f"La letra es {PrimeraLetra}")
        subcantidad = int(input("Bienvenido ingrese la cantidad de nombre que va a ingresar a la lista con esa letra "))
        for x in range(subcantidad):
            valor = str(input("Ingrese la palabra con ese nombre "))
            sublista.append(valor)
        diccionario[PrimeraLetra] = sublista
    return diccionario
print(convertir(nombres))

cantidad = int(input("Bienvenido ingrese la cantidad de palabras que va a ingresar a la lista "))
palabras = []

for p in range(cantidad):
    word = str(input("Ingrese la palabra "))
    palabras.append(word)

print(palabras)

def LongitudPalabras(lista):
    diccionario = {}
    for i in lista:
        diccionario[i] = len(i)
    return diccionario

print(LongitudPalabras(palabras))

cantidad = int(input("Bienvenido ingrese la cantidad de claves y valores que va a ingresar a las listas "))
claves = []
valores = []
for p in range(cantidad):
    keys = str(input("Ingrese la clave "))
    claves.append(keys)
    values = str(input("Ingrese el valor "))
    valores.append(values)
print(claves)
print(valores)
def convertirListas(lista1,lista2):
    diccionario = {}
    for i in range(len(lista1)):
        diccionario[lista1[i]] = lista2[i]
    return diccionario
print(convertirListas(claves, valores))
