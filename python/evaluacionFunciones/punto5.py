cantidad = int(input("Bienvenido ingrese la cantidad de palabras que va a ingresar a la lista "))
palabras = []
for p in range(cantidad):
    numero = str(input("Ingrese el nombre "))
    palabras.append(numero)
def palabras_con_vocales(lista):
    diccionario = {}
    vocales = 'aeiou'
    for palabra in lista:
        TieneVocal = False
        for letra in palabra:
            if letra in vocales:
                TieneVocal = True
                break
        if TieneVocal:
            PrimerLetra = palabra[0]
            diccionario[PrimerLetra] = palabra
    return diccionario
print(palabras_con_vocales(palabras))


