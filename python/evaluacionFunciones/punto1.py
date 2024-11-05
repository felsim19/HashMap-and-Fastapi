cantidad = int(input("Bienvenido ingrese la cantidad de numeros que va a ingresar a la lista "))
numeros = []

for p in range(cantidad):
    numero = int(input("Ingrese el numero "))
    numeros.append(numero)

print(numeros)

def ConvertirDiccionario(lista):
    diccionario = {}
    for i in lista:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario


print(ConvertirDiccionario(numeros))






        


        



