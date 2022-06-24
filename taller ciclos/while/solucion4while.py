# Realizar un juego para adivinar un número. Para ello pedir un número N, y luego ir pidiendo
# números indicando “mayor” o “menor” según sea mayor o menor con respecto a N. El proceso termina
# cuando el usuario acierta.




from random import randint, random


n = random,randint(1, 100)
x = 0

while n != x:

    x = int(input(f"intenteta adivinar el numero digitado: "))
    print(n)

    if x > n:
        print(f"el numero digitado es menor...")

    elif x < n:
        print(f"el numero digitado es mayor...")

    else:
        print("felicidades")
