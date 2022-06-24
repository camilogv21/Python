#Dadas 6 notas, escribir la cantidad de alumnos aprobados, condicionados (=3.5) y reprobados.

cont = 0
cont2 = 0

for i in range(6):
    nota = float(input("digite las notas finales "))
    if nota >= 3.5:
        cont += 1
    else:
        cont2 +=0 
print(f"{cont} alumnos aprobaron")