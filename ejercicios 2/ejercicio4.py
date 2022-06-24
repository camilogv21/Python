#E1: Escriba un programa que realice la sumatoria de los números enteros múltiplos de 4 entre 1 y 100. Usar ciclo for

suma = 0
cont = 0
for i in range(1, 101):
    if i % 4 == 0:
        suma += i       #acumulador
        cont += 1       #contador

    
print(f"La suma es: {suma} y la cantidad encontrada es {cont}")


#E2: Escriba un programa que pida 20 números enteros, averiguar si son múltiplos de 6 y sumarlos. Usar ciclo for.

suma = 0
cont = 0
for i in range(20):
    dato = int( input(f"Digite un número entero {i}: ") )
    if dato % 6 == 0:
        suma += dato        #acumulador
        cont += 1           #contador

print(f"La suma es: {suma} y la cantidad encontrada es {cont}")