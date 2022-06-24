"""2. Construir un script que le pida dos fechas al usuario y retorne a través de una función:
    a. Si las fechas son iguales.
    b. Sino si la fecha 1 es menor que la fecha 2. Indicar cuántos días hay de diferencia.
    c. De lo contrario decir que las fechas no tienen secuencia."""

from operator import truth


def fecha(dia1,dia2,mes1,mes2):

    if dia1 == dia2 and mes1 == mes2:
        return True
    elif dia1 < dia2 and mes1 < mes2:
        res = 30 - dia2
        res1 = res + dia1
        res2 = mes2 - mes1

    if dia1 < dia2 and mes1 == mes2:
        res1 = (dia2 - dia1)
        
    if res2 == 1:
        res2 = 0
        r = (30*res2) + res1
    print(f"hola {r}")
    


if __name__ == "__main__":
    
    m1 = int(input("digite el numero de un mes: "))
    d1 = int(input("digite una dia: "))

    m2 = int(input("digite un numero de un mes: "))
    d2 = int(input("digite una dia: "))

    f=fecha(d1,d2,m1,m2)

    if f == True:
        print("hola")
    else:
        print(f)