#Determinar cuáles son los múltiplos de 5 comprendidos entre 1 y N
#Usar ciclos while.

N = int(input("Digite un num: "))
a = 1
while a <= N:
    if a % 5 == 0:
        print(f"{a} si el múltiplo de 5")
    else:
        print(a)
    a +=1
