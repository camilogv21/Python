

def depositardinero():

    dep = int(input("cuanto dinero quieres depositar: "))
    if dep > 0:
        return dep
    else:
        print("erroe al depositar dinero")

def retirardinero():

    ret = int(input("cuanto dinero quieres retirar: "))
    if ret > 0:
        return ret
    else:
        print("error al retirar dinero!!!!")

def transferirdinero():
        
    tras = int(input("cuanto dinero quieres transferir: "))
    if tras > 0:
        return tras
    else:
        print("erroe al depositar dinero")

def comprar():
    prod = int(input("QUE PRODUCTO DESEA COMPRAR\n\n"
                    "1- audifonos = 20.000\n"
                    "2- Celular = 40.000\n"
                    "3- Cargador = 8.000\n\n"

                    "4- Quieres hacer otra compra\n\n"

                    "ELIGA UNA OPCION "))
    if prod == 1:
        return 20000
    elif prod == 2:
        return 40000
    elif prod == 3:
        return 8000
    elif prod == 4:
        return 4
    else:
        print("opcion incorrecta")

    

if __name__ == "__main__":

    cliente1 = input("digite tu nombre: ")
    cueta1 = int(input("digite tu numero de cuenta: "))
    saldo1 = int(input("digite el saldo: "))

    cliente2 = input("digite tu nombre: ")
    cueta2 = int(input("digite tu numero de cuenta: "))
    saldo2 = int(input("digite el saldo: "))

    cliente3 = input("digite tu nombre: ")
    cueta3 = int(input("digite tu numero de cuenta: "))
    saldo3 = int(input("digite el saldo: "))




    while True:
        print("="*50)
        opc = int(input("QUE QUIERES REALIZAR:\n\n"
                        "1- Depositar dinero \n"
                        "2- Retirar dinero \n"
                        "3- Transferir dinero \n"
                        "4- Comprar \n"
                        "5- mostrar saldo\n"
                        "6- sali \n\n"
                        "eliga una opcion: "))
        print("="*50)

        if opc < 0 or opc > 6:
            print("opcion incorrecta digita otra!!!")

# condicional para dopositar dinero======================================================
        elif opc == 1:
            opc2 = input("A que cliente desea depositar: ")
            if opc2 == cliente1:
                dep = depositardinero()
                saldo1 = dep + saldo1

            elif opc2 == cliente2:
                dep = depositardinero()
                saldo2 = dep + saldo2

            elif opc2 == cliente3:
                dep = depositardinero()
                saldo3 = dep + saldo3

# condicional para retirar dinero=====================================================
        elif opc == 2:
            opc3 = input("A que cliente desea retirar: ")
            if opc3 == cliente1:
                ret = depositardinero()
                if ret <= saldo1:
                    saldo1 = ret - saldo1
                else:
                    print("no puedes retirar mas dinero de lo que tine en el saldo")

            elif opc3 == cliente2:
                dep = depositardinero()
                if ret <= saldo2:
                    saldo1 = ret - saldo2
                else:
                    print("no puedes retirar mas dinero de lo que tine en el saldo")

            elif opc3 == cliente3:
                    dep = depositardinero()
                    if ret <= saldo3:
                        saldo1 = ret - saldo3
                    else:
                        print("no puedes retirar mas dinero de lo que tine en el saldo")

# condicional para trtansferir dinero====================================================
        elif opc == 3:
            opc4 = input("Ingrese el cliente de donde va hacer la tarnsferencia ")
            if opc4 == cliente1:
                tras = input("A que cliente desea hacer la transferencia: ")
                if tras == cliente2:
                    tran = transferirdinero()
                    if tran < saldo1:
                        saldo2 = tran + saldo2
                        saldo1 = tran - saldo1
                    else:
                        print("no puedes tranferir mas deinero de lo que tiene")

                elif tras == cliente3:
                    tran = transferirdinero()
                    if tran < saldo1:
                        saldo3 = tran + saldo3
                        saldo1 = tran - saldo1
                    else:
                        print("no puedes tranferir mas deinero de lo que tiene")

                else:
                    print("el cliente digitado no existe")

            elif opc4 == cliente2:
                tras = input("A que cliente desea hacer la transferencia: ")
                if tras == cliente1:
                    tran = transferirdinero()
                    if tran < saldo2:
                        saldo1 = tran + saldo1
                        saldo2 = tran - saldo2
                    else:
                        print("no puedes tranferir mas deinero de lo que tiene")

                    
                elif tras == cliente3:
                    tran = transferirdinero()
                    if tran < saldo2:
                        saldo3 = tran + saldo3
                        saldo2 = tran - saldo2
                    else:
                        print("no puedes tranferir mas deinero de lo que tiene")
                    

                else:
                    print("el cliente digitado no existe")

            elif opc4 == cliente3:
                tras = input("A que cliente desea hacer la transferencia: ")
                if tras == cliente1:
                    tran = transferirdinero()
                    if tran < saldo2:
                        saldo1 = tran + saldo1
                        saldo3 = tran - saldo3

                    else:
                        print("no puedes tranferir mas deinero de lo que tiene")
                    
                elif tras == cliente2:
                    tran = transferirdinero()
                    if tran < saldo2:
                        saldo2 = tran + saldo2
                        saldo3 = tran - saldo3

                    else:
                        print("no puedes tranferir mas deinero de lo que tiene")

                else:
                    print("el cliente digitado no existe")

# condicional para comprar productos===================================================


        elif opc == 4:
            opc5 = input("ingrese el cliente para hacer una compra: ")

            if opc5 == cliente1:
                
                do = True
                while do:
                    com = comprar()
                    if com < saldo1:
                        print ("compra realizada")
                        saldo1 = com - saldo1
                    elif com > saldo1:
                        print("no tienes suficiente saldo")
                    else:
                        do = False
                     

            elif opc5 == cliente2:

                do = True
                while do:
                    com = comprar()
                    if com < saldo2:
                        print ("compra realizada")
                        saldo1 = com - saldo2
                    elif com > saldo2:
                        print("no tienes suficiente saldo")
                    else:
                        do = False

            elif opc5 == cliente3:

                do = True
                while do:
                    com = comprar()
                    if com < saldo3:
                        print ("compra realizada")
                        saldo1 = com - saldo3
                    elif com > saldo3:
                        print("no tienes suficiente saldo")
                    else:
                        do = False
    
# condicional para mostrar saldo===================================================

        elif opc == 5:
            opc6 = input("Que cliente quiere mirar el saldo: ")
            if opc6 == cliente1:
                print(f"este es tu saldo {saldo1}")

            elif opc6 == cliente2:
                print(f"este es tu saldo {saldo2}")

            elif opc6 == cliente3:
                print(f"este es tu saldo {saldo3}")

# condicional para salir============================================================

        elif opc == 6:
            print(f"saldo de {cliente1} es {saldo1}")
            print("="*50)

            print(f"saldo de {cliente2} es {saldo2}")
            print("="*50)

            print(f"saldo de {cliente3} es {saldo3}")

            break

        else:
            print("opcion incorrecta!!!!")

