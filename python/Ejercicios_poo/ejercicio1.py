#  Crea una clase `Calculadora` que tenga métodos para realizar operaciones matemáticas como suma, resta, multiplicación y división.

class calculadora:

    def __init__(self, NumeroA, NumberoB):
        self.NumeroA = NumeroA
        self.NumeroB = NumberoB

    def obtenerA(self):
        return self.NumeroA
    
    def obtenerB(self):
        return self.NumeroB
    
    def suma(self):
        A = self.NumeroA
        B = self.NumeroB
        return (A + B) 
    
    def resta(self):
        A = self.NumeroA
        B = self.NumeroB
        return (A - B)
    
    def multiplicar(self):
        A = self.NumeroA
        B = self.NumeroB
        return (A * B)
    
    def Dividir(self):
        A = self.NumeroA
        B = self.NumeroB
        return (A / B)