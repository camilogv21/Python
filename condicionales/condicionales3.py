

num = int(input("digite u numero: "))

if num % 2 == 0:
    if num < 0:
        print(f"el numero es par y es negativo: {num}")
    else:
        print(f"el numero es par y positivo: {num}")
else:
    if num < 0:
        print(f"el numero es impar y negativo: {num}")
    else:
        print(f"el numero es impar y positivo: {num}")
