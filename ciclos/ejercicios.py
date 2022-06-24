""" determinar cuales son los multiplos de 5 entre 1 y n usar el ciclo while mod en python es %"""

num = int(input("digite un numero "))
a = 1


while a <= num:
    b = a % 5
    if b == 0:
        print(f"el numero {a} es multiplo de 5")
    a +=1
    