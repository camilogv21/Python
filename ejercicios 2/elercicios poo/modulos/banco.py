import random


class Banco:
    def _imit_(self):
        self.propietario = ""
        self.estado = ""
        self.saldo = 0
        self.numCuenta = 0
        
    def crearCuenta(self):
        self.numCuenta = random.randint(5000 , 6000)
        self.propietario = input("digite el nombre del propietario: ")
        self.saldo = 0
        
    def estadoCuenta(self):
        
        if self.saldo < 0:
            self.estado = "inactiva"
        else:
            self.estado = "activa"
            
    def depositarDinero(self):
        self.cant = int(input("cuento dinero desea consignar: "))
        self.saldo = self.cant + self.saldo
        
    def transferirDinero(self):
        if self.estado == "activa":
            self.tran = int(input("cuanto dinero quiere tranferir: "))
            self.saldo = self.saldo - self.tran
        else:
            print("Tu cuenta esta inactiva")
            
    def menu(arg):
        pass
        
    
        
        
    def __str__(self) -> str:
        return f"=====================\nMi cuenta es: {self.numCuenta}\nEl propietario es: {self.propietario}\nEl estado es: {self.estado}\nEl saldo es: {self.saldo}\n====================="
    
if __name__ == "__main__":
    print(f"No soy un archivo principal")