print('Bienvenido a Python" Code!')

num1 = 20
print( type(num1) )
#comentario sencillo
""" comentario múltiple """

num1 = 3.5

num1 = False
num1 = True
num1 = "Hola mundo!"

import datetime

num1 = datetime.datetime.now()
print( num1 )

num1 = datetime.datetime(2022, 1, 28)
print( num1 )


num2 = input("Digite su edad: ")
print("Usted tiene ", num2, " años.")
#casting  -> Transformación entre tipos de datos
"""
str (string)    -> cadena
int (integer)   -> entero
float (real)    -> decimal
"""

print(type(num2))

num2 = int(num2)
num2 = float(num2)
num2 = bool(num2)
num2 = str(num2)

num2 = int( input("Digite su edad: ") )
print(type(num2))
print("Usted tiene ", num2, " años.")


nota1 = float( input("Digite su nota: ") )

print("La nota es:", nota1)

print(f"La nota es: {nota1} y esto {num1} sss {num2}")

