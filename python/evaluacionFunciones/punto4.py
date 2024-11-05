cantidad = int(input("Bienvenido ingrese la cantidad de numeros que va a ingresar a la lista "))
numeros = []
for p in range(cantidad):
    numero = int(input("Ingrese el numero "))
    numeros.append(numero)
def devolver(lista):
    diccionario = {}
    for n in numeros:
        primo = True
        if n < 2:
            primo = False
        else:
            for j in range(2,int(n**0.5) + 1):
                if n % j == 0:
                    primo = False
                    break
        diccionario[n] = primo
    return diccionario
print(devolver(numeros))



cantidad = int(input("Bienvenido ingrese la cantidad de productos y precios que va a ingresar al dicionario "))
productos = {}
for p in range(cantidad):
    product = str(input("Ingrese el producto "))
    price = int(input("Ingrese el precio "))
    productos[product] = price
print(productos)
def listaOrdenada(dicionario):
    lista = []
    while dicionario:
        menor_precio = 99999
        producto_menor = ''
        for producto, precio in dicionario.items():
            if precio < menor_precio:
                menor_precio = precio
                producto_menor = producto
        lista.append((producto_menor, menor_precio))
        del dicionario[producto_menor] 
    return lista
print(listaOrdenada(productos))
