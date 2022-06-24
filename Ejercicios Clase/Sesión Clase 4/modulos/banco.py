import random

class Banco:
    cuentas = []
    def __init__(self):
        self.cuenta = 0
    
    def crearCuenta(self):
        self.cuenta = random.randint(5000, 6000)

    def __str__(self) -> str:
        return f"Mi cuenta es {self.cuenta}"

if __name__ == "__main__":
    print(f"No soy un archivo principal")
