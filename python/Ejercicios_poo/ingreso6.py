from ejercicio6 import Vuelo

vuelo1 = Vuelo("Bogota","Santa Marta", 50)

while(True):
    op = int(input("1.reservar\n2.consultar\n3.salir\n"))
    if(op == 1):
        asientos = int(input("cuantos asientos quiere comprar? "))
        vuelo1.reservar_asientos(asientos)
    elif(op == 2):
        vuelo1.consultar_asientos()
    elif(op == 3):
        print("adiosss")
        break