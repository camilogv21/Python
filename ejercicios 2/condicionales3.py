#Averiguar si un número es par o impar.
#Luego, de forma anidada averiguar si es + o -
num = int(input("Digite un num entero: "))

if num % 2 == 0:
    print(f"El num {num} es par")
    if num < 0:
        print("es negativo")
    else:
        print("es positivo")
else:
    print(f"El num {num} es impar")
    if num < 0:
        print("es negativo")
    else:
        print("es positivo")
    
print("fin")