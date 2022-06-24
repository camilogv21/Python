"""7. Construir un script que valide si un correo electrónico está escrito correctamente (sólo validar los ítems
    a, b y c, dado que no es una validación completa). Para ello debe solicitar el correo electrónico al
    usuario y a través de una función verifique:

    a. Que por lo menos exista una @ y un punto (.)
    b. Sólo puede haber una arroba @ y máximo dos puntos en la cadena.
    c. Por lo menos antes de la arroba @ debe haber 3 caracteres.
    d. Si se cumplen las condiciones anteriores mostrar: Correo electrónico Correcto, de lo contrario
    mostrar: Correo erróneo."""

def funcion(correo,c,d,b):

    for a in correo:
        b += 1
        if a == "@":   
            break

    for a in correo:

        if a == "@":   
            d += 1
        elif a == ".":
            c += 1
    v = b - 1       
    if d >= 1 and c >= 2 and v >= 3:
        print(f"correo electronico correcto {v} ")
    else:
        print("correo erroneo")
    
if __name__ == "__main__":

    ar = 0
    pu = 0
    le = 0
    co = str(input("digite tu correo: "))

    t = funcion(co,pu,ar,le)
    print(t)
