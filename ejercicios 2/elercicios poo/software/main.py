import config
from banco import Banco

if __name__ == "__main__":
    
       
    
    print("**** MENU DEL BANCO ****")
    print("1- Crear cliente\n"
          "2- Consignar dinero\n"
          "3- Transferir dinero\n")
    
    opc = int(input("Escoge una opcion: "))
    
    u1 = Banco()
    u2 = Banco()
    u1.crearCuenta()
    u2.crearCuenta()
    u1.estadoCuenta()
    u2.estadoCuenta()

    print(u1)
    print(u2)
    
    u1.depositarDinero()
    u2.depositarDinero()
    u1.estadoCuenta()
    u2.estadoCuenta()
      
    print(u1)
    print(u2)

    u1.transferirDinero()
    u2.transferirDinero()
    u1.estadoCuenta()
    u2.estadoCuenta()
    
    print(u1)
    print(u2)