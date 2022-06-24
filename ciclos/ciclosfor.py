#escriba un progroma que realice la sumatoria de los numeros enteros mutiplos de 4 entre 1 y 100 usar ciclo for#

suma = 0
cont = 0
for i in range(1, 101):
    if i % 4 == 0:
        suma += i
        cont += 1
print (f"la suma de los numeros es: {suma}, el toltal de los numeros encontrados  son: {cont} de {i}")



#escriba un programa que pida 20 numeros enteros. averiguar si es multiplo de 6 y sumarlos usar ciclo for#


suma = 0
cont = 0
for x in range(20):
    dato=int (input("digite un numero : "))
    if dato % 6 == 0:
        suma += x
        cont += 1
print (f"la suma de los numeros es: {suma}, el toltal de los numeros encontrados son: {cont} de {x}")