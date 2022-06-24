#ejercicio2: construir una funcion que convierta un numero en negativo
#           nota: si ya es negativo no lo convierta


def negativo(numero,):
    r = (numero * -1)
    return r

if __name__=="__main__":

    num = int(input("digite un numero para convertir: "))

    b = (num *-1)

    if num > 0:
        print(f"el numero en nagativo es: {b}")
    else:
        print(f"el numero ya es negativo: {num}")

