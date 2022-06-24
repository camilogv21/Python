"""5. Construya una función que calcule cuántas páginas de 10 registros (es decir páginas de 10 en 10) salen
    de un número de registros (pedirlo al usuario en zona de algoritmo). Nota, controlar que el dato pedido
    sea mayor que cero."""

def funcion(registro):

    if registro % 10:
        a = registro / 10
        b = int(a) * 10
        c = registro - b
        d = (b / 10) + 1
        print(f"{registro} registros generan {d} páginas, la última queda con {c} registros.")
    else:
        a = registro / 10
        print(f"{registro} registros generan {a} páginas" )

if __name__ == "__main__":

    reg = int(input("digite el numero de resgistros: "))

    if reg <= 0:
        print("el numero del registro debe ser mayor a 0")
    else:
        r = funcion(reg)
        print(r)

