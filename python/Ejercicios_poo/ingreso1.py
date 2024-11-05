#  Crea una clase `Calculadora` que tenga métodos para realizar operaciones matemáticas como suma, resta, multiplicación y división.

from ejercicio1 import calculadora

while(True):
    op = int(input(f"Bienvenido, que desear hacer usuario? \n1.sumar\n2.restar\n3.multiplicar\n4.dividir\n5.salir\n"))
    if(op < 5):
        numeroa = int(input("Digite El Primer Numero "))
        numerob = int(input("Digite el segundo numero "))
        calcular = calculadora(numeroa,numerob)
        if(op == 1):
            print(f"{calcular.obtenerA()} + {calcular.obtenerB()} = {calcular.suma()}")
        elif(op == 2):
            print(f"{calcular.obtenerA()} - {calcular.obtenerB()} = {calcular.resta()}")
        elif(op == 3):
            print(f"{calcular.obtenerA()} x {calcular.obtenerB()} = {calcular.multiplicar()}")
        elif(op == 4):
            print(f"{calcular.obtenerA()} / {calcular.obtenerB()} = {calcular.Dividir()}")
    elif(op == 5):
        print("Adios usuario, que este bien")
        break
    elif(op > 5):
        print("digite un numero que corresponda") 
         
     
        
