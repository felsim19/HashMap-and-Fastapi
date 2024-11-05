#Crea una clase `Producto` con atributos como nombre, precio y cantidad en stock. Implementa métodos para añadir productos, actualizar stock y calcular el valor total del inventario.

from ejercicio4 import Productos
manejoProductos = Productos()
while(True):
    op = int(input("1.añadir opcion \n2.Actualizar stock\n3.Mostrar Lista\n4.cacular valor Inventario\n5.salir\n"))
    if(op == 1):
        producto = str(input("Digite el nombre del producto "))
        precio = float(input("Digite el precio del producto "))
        cantiad = int(input("Digite la cantidad de ese producto "))
        producto = manejoProductos.agregar_producto(producto,precio,cantiad)
        manejoProductos.agregar_lista(producto)
    elif(op == 2):
        nombre = str(input("Digite el nombre del producto que esta buscando "))
        manejoProductos.actualizar_stock(nombre)
    elif(op == 3):
        manejoProductos.mostar_lista()
    elif(op == 4):
        manejoProductos.valor_inventario()
    elif(op == 5):
        print("usted esta saliendo del programa")
        break
    
