#Leer números hasta que se introduzca un 0. Para cada uno indicar si es par o impar.#

from random import randint, random


dato = randint(0, 100)

while dato > 0:
    dato = randint(0, 100)
    if dato == 0:
        print(f"el numero leido es un {dato}")
    elif dato % 2 == 0:
        print(f"el numero {dato} es un numero par")
    else:
        print(f"el numero {dato} es un numero impar")
                                                                                