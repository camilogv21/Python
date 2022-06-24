"""4. Construir un script que le pregunte al usuario la hora de llegada de un carro al llegar al parqueadero y
    la hora de salida. Usando una función calcular el valor a pagar, sabiendo que el parqueadero cobra por
    hora o fracción $2000.
    Nota: Los carros no pueden quedarse de un día para otro. Usar hora militar para pedir los datos. La
    hora inicial debe ser anterior a la hora final."""

def funcion(horaentrada,horasalida,minutoentrada,minutosalida):
    h = horasalida - horaentrada
    m = minutoentrada + minutosalida
    v = 2000

    if m > 60:
        f = m-60
        a = h + 1
        r = h * v
        print(f"usted estuvo {h} horas con {f} minutos el total a pagar es: {r} ")
    elif horasalida == horaentrada:
        m = minutosalida - minutoentrada
        print(f"usted estuvo {m} minutos en el parqueadero desbes pagar {v}")
    else:
        r = h * v
        print(f"usted estuvo {h} horas con {f} minutos el total a pagar es: {r} ")



if __name__ == "__main__":


    he = int(input("ingrese la hora de entrada: "))
    me = int(input("ingrese los minutos de entrada: "))
    hs = int(input("ingrese la hora de salida: "))
    ms = int(input("ingrese los minutos de salida: "))

    f = funcion(he,hs,me,ms)

    if he > hs:
       print("!!! ERROR LA HORA DE LLEGADA NO PUEDE SER MAYOR A LA HORA DE SALIDA !!!")
    else:
        print(f)
    
    
    
    