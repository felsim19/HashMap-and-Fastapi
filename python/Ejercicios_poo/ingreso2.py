#Diseña una clase `CuentaBancaria` que almacene el saldo y permita realizar operaciones como depósito y retiro

from ejercicio2 import CuentaBancaria

saldo = int(input("Binvenido usuario usted va a crear una cuenta \nPor favor ingrese el monto del saldo de la cuenta que acabo de crear\n"))

cuenta1 = CuentaBancaria(saldo)

while(True):
    op = int(input("Bienvenido usuario \n1.depositar \n2.retirar \n3.consultar saldo \n4.salir\n"))
    if(op == 1):
        deposito = int(input("Digite cuanto va a depositar a la cuenta "))
        cuenta1.DepositarSaldo(deposito)
        print(f"Bien , su cuenta ahora tiene un saldo de {cuenta1.ObtenerSaldo()}")
    elif(op == 2):
        retiro = int(input("Digite cuanto va a retirar de la cuenta "))
        cuenta1.RetirarSaldo(retiro)
        print(f"Bien , su cuenta ahora tiene un saldo de {cuenta1.ObtenerSaldo()}")
    elif(op == 3):
        print(f"Su saldo actual es de {cuenta1.ObtenerSaldo()}")
    elif(op == 4):
        print("Adios usuario")
        break
    else:
        print("Eliga un numero correcto")
        