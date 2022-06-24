"""
Crear 3 LISTAS (Nombres, Cargos, Sueldos)
Usar 1 función para aumentar el sueldo en los siguientes casos:
    Si el empleado gana entre $1 millon y $2 millones, aumentar 20%
    Si el empleado gana más de $8 millones, aumentar 3%
    Sino, no hacer aumento.

Pedir al usuario del software la cantidad de empleados.
solicitar:
    Nombre, Cargo y Sueldo de cada uno de ellos.
    Almacenar en cada lista los datos y el nuevo sueldo calculado

Al final imprimir todo de la siguiente manera: EJEMPLO

Nombre              Cargo       Sueldo
Pedro Martelo       Jefe        9.000.000       (ojo calcular con uso de función)
Ana Pérez           Secretaria  1.500.000       (ojo calcular con uso de función)
Marta Lucía H.      Abogada     5.000.000       (ojo calcular con uso de función)
.
.
Bonito: Se llama caracter especial para tabulador en print.
"""
def aumentarSueldo(sueldo):
    if sueldo >= 1000000 and sueldo <= 2000000:
        return sueldo * 1.2
    elif sueldo >= 8000000:
        return sueldo * 1.03
    else:
        return sueldo


if __name__ == "__main__":
    nombres = []
    cargos = []
    sueldos = []

    n = int(input("Cantidad de empleados: "))

    for i in range(n):
        nom = input(f"{i}. Digite su nombre: ")
        cargo = input(f"{i}. Digite su cargo: ")
        suel = int(input(f"{i}. Digite su sueldo: "))

        nombres.append(nom)
        cargos.append(cargo)
        sueldos.append(aumentarSueldo(suel))

    print(f"Nombre\t\t\t|Cargo\t\t\t|Sueldo")
    print("="*50)
    for i in range(n):
        print(f"{nombres[i]}\t\t\t|{cargos[i]}\t\t\t\t|{sueldos[i]}\r")


#secuencias de escape (... de caracteres)
print('I don\'t know.')

from tabulate import tabulate

pip install tabulate
pip3 install tabulate
