#ciclo for              (para)

#range(5)               0 al 4
#range(20)              0 al 19

#range(1, 5)            1 al 4
#range(1, 8)            1 al 7
#range(5, 8)            5 al 7

#range(1, 5, 1)         1 al 4 con paso 1
#range(1, 5, 2)         1 al 4 con paso 2
#range(X, N)            1 al N-1

#range(10, 1, -1)       10 al 2 con paso -1

listado = list(range(10, 8, -1))
print(f"Vector: {listado}")

for i in listado:
    print(i)

print("-"*20)

listado = list(range(1, 8, 1))
print(f"Vector: {listado}")

for i in listado:
    print(i)