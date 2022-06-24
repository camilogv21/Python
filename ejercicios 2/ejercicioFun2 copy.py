"""Llenar dos LISTAS (usuarios y passwords) (pedir 3 registros al usuario):

jor     -> usuarios     0
12345   -> passwords    0

admin   -> usuarios     1
9789    -> passwords    1

Simular un login y cerrado de sesión
Validar estados. ****** Función ************

opt = int(input('''
Un menú que pregunte (do-while):
1. Loguearse
2. Cerrar Sesión
3. Salir
'''))
Controlar la variable "logueado" True|False
"""
def autentica(uu, pp):
    global logueado, users, passw
    #averiguar e iniciar sesión
    for i in range(3):
        if users[i] == uu and passw[i] == pp:
            #Usuario y pasword encontrados!!
            logueado = True
            break

def cerrarSesion():
    global logueado
    if logueado == True:
        logueado = False
        


if __name__ == "__main__":
    
    logueado = False

    print("Lenado de LISTAS")
    print("="*15)

    users = []  #lista
    passw = []  #lista
    for i in range(3):
        u = input("Digite el usuario: ")
        p = input("Digite el password: ")
        users.append(u)
        passw.append(p)

    print("Base de Datos")
    print("="*15)
    for i in range(3):
        print(f"Usuario: {users[i]} - Password: {passw[i]} ")


    opt = 0
    while opt != 3:
        opt = int(input('''
        Que desea hacer?:
        1. Loguearse
        2. Cerrar Sesión
        3. Salir
        '''))

        if opt == 1:
            if logueado == False:
                us = input("Digite el usuario: ")
                pa = input("Digite el password: ")
                autentica(us, pa)
                if logueado:
                    print("Bienvenido, se inicia sesión")
                else:
                    print("Usuario o Password no válidos")
            else:
                print("Usted ya tiene una sesión abierta...")

        elif opt == 2:
            cerrarSesion()
            if logueado:
                print("Sesión cerrada correctamente!")
            else:
                print("Usted NO tiene sesión abierta.")
            

    print("Chao!")