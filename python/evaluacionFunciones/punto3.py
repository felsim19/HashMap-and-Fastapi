cantidad = int(input("Bienvenido ingrese la cantidad de estudiantes que va a ingresar a la lista "))
nombres = []
notass = []
for p in range(cantidad):
    nombre = str(input("Ingrese el nombre "))
    nombres.append(nombre)
    calif = int(input("Digite cuantas calificaiones tiene el estudiante "))
    promedio = 0
    for x in range(calif):
        notas = int(input("Digite sus calificaciones "))
        promedio += notas
    total = promedio / calif
    notass.append(total)        
print(nombres)
print(notass)
def convertir(listanombre,listanotas):
    diccionario = {}
    for i in range(len(listanombre)):
        diccionario[listanombre[i]] = listanotas[i]
    return diccionario    
print(convertir(nombres,notass))

cantidad = int(input("Bienvenido ingrese la cantidad de nombre y edades que va a ingresar al dicionario "))
dicionario = {}
for p in range(cantidad):
    name = str(input("Ingrese el nombre "))
    age = int(input("Ingrese la edad "))
    dicionario[name] = age   
def menor(dicionario):
    minor = 999
    nameMinor = ''
    for nombre, menor in dicionario.items():
        if menor < minor:
            minor = menor
            nameMinor = nombre
    return minor,nameMinor
print(menor(dicionario))







cantidad = int(input("Bienvenido ingrese la cantidad de productos y precios que va a ingresar a las listas "))
productos = []


for p in range(cantidad):
    product = str(input("Ingrese el producto "))
    productos.append(product)
    price = str(input("Ingrese el precio "))
    productos.append(price)

print(productos)


def productoCaro(lista1):
    diccionario = {}
    mayor = 0
    for i in range(0,len(lista1),2):
        precio = float(lista1[i])
        if mayor < precio:
            mayor = precio
    indice = lista1.index(str(mayor))
    nombre = lista1[indice -1] 
    diccionario[mayor] = nombre   
    return diccionario

print(productoCaro(productos))

