"""
Desarrolle un script en python que lea un num por teclado.
En caso de que sea cero(0) terminar el programa y mostrar un mensaje de error.
Si es mayor que cero. se debera calcular su cuadrado y la raíz cuadrada del mismo. Mostrar resultado de la siguiente manera: 
<<<< Del número x, su potencia es X y su raiz es Y >>>
Si es menor que cero. Convertir el número a positivo.

Nota: Para calcular la raíz se puede usar la librería:
import math
y usar la función:
math.sqrt(x)
"""
import math

num = int(input("Digite un num: "))

if num == 0:
    print("Error")
elif num > 0:
    #cuad = num * num
    #cuad = math.pow(num, 2)
    cuad = num ** 2
    raiz = math.sqrt(num)
    print(f"Del número {num}, su potencia es {cuad} y su raiz es {raiz:0.2f}")
elif num < 0:
    pos = num * -1
    #pos = abs(num)
    print(f"El número {num} convertido a positivo es: {pos}")

