numero = int(input("Ingrese hasta que numero desea saber "))
def fibonacci(numero):
    fibonacci = [0,1]
    for i in range(numero):
        fibonacci.append(fibonacci[-1] + fibonacci[-2]) 
    return fibonacci
print(fibonacci(numero))


numero = int(input("Ingrese hasta que numero desea saber "))
def calcular(numero):
    descomponer = str(numero)
    calcular = 0
    for digito in descomponer:
        calcular += int(digito)
    cantidad = str(calcular)
    total = len(cantidad)
    return calcular, total
suma, cantidad = calcular(numero)
print(f"El numero es {numero} y la suma de sus digitos es de {suma} y la cantidad de los digitos es de {cantidad}")

