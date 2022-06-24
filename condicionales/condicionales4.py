
""""
desarolle un script en python que lea un numero por teclado.

en caso de que sea cero terminar el programa y mostrar un
mensaje de error.

si es mayor a cero. se debera calcular su cuadrado y la 
raiz cuadrada del mismo. mostrar resultados del siguiente
manera: <<<<< del numero x, su potencia x y su raiz es y

si es menor que cero. convertir el numero a positivo


nota: para calcular la raiz se puede usa la libreria:
import math
y usar la formacion 
math.sqrt(x)
...

"""




a = int(input("digite un numero: "))

if a >= 1:
    cuan = a * a
    import math
    raiz = math.sqrt ( a )
    print(f"del numero: {a} su potencia es: {cuan} y su raiz es: {raiz}") 
elif a <= -1:
     pos = a * -1
     print(f"el numero en positivo es: {pos}")
else:
    print("ERROR el numero no es negativo ni positivo")

