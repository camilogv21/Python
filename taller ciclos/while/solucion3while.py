#Pedir números hasta que se teclee uno negativo, y mostrar cuántos números se han introducido.


dato = 0
cont = 0
while dato > -1:
    dato = int(input("digite un nemero que no sea negativo: "))
    if dato > -1:
        cont += 1
    else:
        print("¡¡¡digito un numero incorrecto")
print(f"numeros digitados correctamente son: {cont}")
