class Productos:
    def __init__(self):
        self.lista = [("camiseta", 25.000),
                    ("pantalones", 35.000),
                    ("zapatos", 120.000),
                    ("sombrero", 20.000),
                    ("bufanda", 10.100)]
        self.carrito = []
        self.valor_total = 0
    
    def mostrar_productos(self):
        print("los productos disponibles son estos : ")
        for i in self.lista:
            print(i)
            
    def añadir_carrito(self,nombre):
        for i in range(len(self.lista)):
            if nombre == self.lista[i][0]:
                cantidad = int(input("Ingrese cuantas cantidades quiere de este producto "))
                for x in range(cantidad):
                    self.carrito.append(self.lista[i])
                print("Productos añadidos correctamente ")
                
    def mostrar_carrito(self):
        print("el carrito cuenta con estos productos : ")
        for i in self.carrito:
            print(i)
            
    def total_carrito(self):
        total = 0
        for nombre, precio in self.carrito:
            total += precio
        self.valor_total = total
        return print(f"El total que tiene que pagar para llevarse los productos son : {self.valor_total}")
    
    def pagar(self, total):
        if self.valor_total == total:
            print("¡Felicidades! Ha pagado el producto.")
            self.valor_total = 0
            self.carrito.clear()  
        else:
            print(f"Ingrese la cantidad total correcta para pagar. El total es ${self.valor_total}")
                         
                