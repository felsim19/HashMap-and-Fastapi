from ejercicio8 import Productos

manejo_productos = Productos()

while(True):
    op = int(input("1.Mostar productos\n2.añadir productos al carrito\n3.ver carrito\n4.calcular el total\n5.realizar el pago\n6.salir\n"))
    if(op == 1):
        manejo_productos.mostrar_productos()
    elif(op == 2):
        nombre = str(input("Digite el nombre del producto que desea añadir ")).lower()
        manejo_productos.añadir_carrito(nombre)
    elif(op == 3):
        manejo_productos.mostrar_carrito()
    elif(op == 4):
        manejo_productos.total_carrito()
    elif(op == 5):
        total = float(input("Que cantidad de dinero va a dar? "))
        manejo_productos.pagar(total)
    elif(op == 6):
        print("adiiiioos")
        break