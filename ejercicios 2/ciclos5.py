#Matrices o Listas multidimensionales o Vectores n-dimensionales
matriz = [ [1,2,3], [4,5,6], [7,8,9] ]

print(f"Coordenada específica (1,2): {matriz[1][2]}")

cont = 0
for renglon in matriz:
    #print(f"El del medio es: {i[0]}")
    """print(f"Renglón({cont}): {renglon}")"""
    #print("-"*20)
    cont2 = 0
    for j in renglon:
        print(f"Coordenada({cont},{cont2}) Valor: {j}")
        cont2 += 1

    cont += 1
    