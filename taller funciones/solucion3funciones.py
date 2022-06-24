"""3. Construir un script que revise si dos horas están ordenadas a través de una función (enviar los cuatro
    argumentos). Imprimir en la zona del algoritmo. Usar hora militar."""

def funcion(hora1,hora2,minuto1,minuto2):
    if hora1 > hora2:
        if minuto1 > minuto2:
            print(f"!!! ERROR !!! la hora {hora1} con minutos {minuto1} es mayor a la hora {hora2} con minutos {minuto2}")
    elif hora1 == hora2:
        if minuto1 == minuto2:
            print(f"la hora {hora1} con minutos {minuto1} es igual a la hora {hora2} con minutos {minuto2}")
        elif minuto1 > minuto2:
            print(f"!!! ERROR !!! la hora {hora1} con minutos {minuto1} es mayor a la hora {hora2} con minutos {minuto2}")
        else:
            print(f"la hora {hora1} con minutos {minuto1} es menor a la hora {hora2} con minutos {minuto2}")
    else:
        print(f"la hora {hora1} con minutos {minuto1} es menor a la hora {hora2} con minutos {minuto2}")

if __name__ == "__main__":

    h1 = int(input("ingrese una hora: "))
    m1 = int(input("ingrese los minutos: "))
    h2 = int(input("ingrese una hora: "))
    m2 = int(input("ingrese los minutos: "))

    funcion (h1,h2,m1,m2)