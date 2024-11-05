#Diseña una clase `CuentaBancaria` que almacene el saldo y permita realizar operaciones como depósito y retiro

class CuentaBancaria:

    def __init__(self,saldo):
        self.saldo = saldo

    def ObtenerSaldo(self):
        return self.saldo
    
    def DepositarSaldo(self, deposito):
        self.saldo += deposito
        return self.saldo
    
    def RetirarSaldo(self, retiro):
        resta = self.saldo - retiro
        if resta < 0:
            print("No puede retirar, si al retirar deja la cuenta en menos de 0")
        else:
            self.saldo -= retiro
        return self.saldo