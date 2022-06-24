#Pide un número (que debe estar entre 0 y 10) y mostrar la tabla de multiplicar de dicho
#número


num = int(input("digite un numero: "))

cont = 0

while cont < 10:
    cont += 1
    mul=(cont * num)
    print(f"{num} x {cont} = {mul}")