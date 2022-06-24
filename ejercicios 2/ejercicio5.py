#ciclo for, listas y valores aleatorios

import random

#d1 = random.randint(1, 6)


vector = []
for i in range(5):
    dato = random.randint(1, 20)
    if dato == 5: 
        break
    #dato = input("Digite un valor: ")
    vector.append(dato)

tam = len(vector)
print(f"El tamaño del vector es: {tam}")


for i in vector:
    print(f"{i}", end=" - ")

print()

vector.pop(0)           #eliminar por índice
vector.remove(17)       #eliminar por valor 

for i in vector:
    print(f"{i}", end=" - ")

print()



