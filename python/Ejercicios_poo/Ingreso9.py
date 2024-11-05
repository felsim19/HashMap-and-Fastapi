from ejercicio9 import Paquete

origen = str(input("Bienvenido ingrese la ciudad de origen del paquete "))
destino = str(input("Bienvenido ingrese la ciudad de destino del paquete "))

envio = Paquete(origen, destino)

inprogram = True

while(inprogram):
    r = int(input("1.Cambiar estado\n2.Consultar Ubicacion\n3.Mostra los productos\n4.salir\n"))
    if(r == 1):
        estadoNuevo = str(input("Digite el nuevo estado "))
        envio.EditarEstado(estadoNuevo)
    elif(r == 2):
        print(envio.ConsultarUbicacion())
    elif(r == 3):
        print(envio.__str__())
    elif(r == 4):
        inprogram = False