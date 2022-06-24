def promedio(nota1,nota2,nota3):
    r = (nota1 + nota2 + nota3) / 3
    return r

if __name__=="__main__":
    n1 = float(input ("digite su nota: "))
    n2 = float(input ("digite su nota: "))
    n3 = float(input ("digite su nota: "))

    res = (n1+ n2+ n3) / 3
    
    print(f"el promedio es: {res}")
    print(f"el promedio es: {(n1+ n2+ n3) / 3}")