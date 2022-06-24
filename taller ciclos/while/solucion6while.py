
#Pide un número (que debe estar entre 0 y 10) controlar que hasta que
#esto no ocurra no pase a lo siguiente que es: mostrar la tabla de multiplicar de dicho número.

cont = 0

while True:
    num = int(input("digite un numero entre 0 y 10: "))
    if num < 0 or num > 11:
        print("error!!!")
    elif num >= 0:
        break
if num <= 10 and num >= 0 :
    while True:
        cont += 1
        if cont <= 10:  
            mul=(cont * num)
            print(f"{num} x {cont} = {mul}")
        elif cont >= 10:
            break
        

