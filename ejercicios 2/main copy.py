def promedio(nota1, nota2, nota3):
    r = (nota1 + nota2 + nota3) / 3
    return r


if __name__ == "__main__":
    n1 = float(input("Digite su nota: "))
    n2 = float(input("Digite su nota: "))
    n3 = float(input("Digite su nota: "))

    res = promedio(n1, n2, n3)

    print (f"El resultado es {res} ", end="")
    print (f"El resultado es {promedio(n1, n2, n3)} ")
