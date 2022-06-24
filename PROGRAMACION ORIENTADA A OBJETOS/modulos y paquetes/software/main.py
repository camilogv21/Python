import config
from banco import Banco

if __name__ == "__main__":
    
    u1 = Banco()
    u2 = Banco()
    u1.crearCuenta()
    u2.crearCuenta()
    print(u1)
    print(u2)