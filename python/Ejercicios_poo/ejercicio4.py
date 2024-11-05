class Productos:
    def __init__(self):
        self.lista = []
        
    def agregar_producto(self, nombre, precio, cantidad_en_stock):
        Producto = (nombre,precio,cantidad_en_stock)
        return Producto

    def agregar_lista(self, Producto):
        self.lista.append(Producto)
        
    def valor_inventario(self):
        valor_total = 0
        for nombre, precio, cantidad in self.lista:
            valor_total += precio * cantidad
            return print(f" el Valor total del inventario es de : {valor_total}")
    
    def actualizar_stock(self, nombre):
        for producto in self.lista:
            if producto[0] == nombre:
                nueva_cantidad = int(input(f"Ingrese la nueva cantidad en stock para '{nombre}': "))
                producto_modificado = (nombre, producto[1], nueva_cantidad)
                index = self.lista.index(producto)
                self.lista[index] = producto_modificado
                print(f"Stock actualizado para '{nombre}'.")
                return
        print(f"No se encontró el producto '{nombre}' en la lista.")
            
    def mostar_lista(self):
        print("lista")
        for i in self.lista:
            print(i)
        
