# ejercicio 1 = pedir nombre al usuario y saludarlo

def saludo():
    return "hola "

if __name__=="__main__":

    nom = input("cual es tu nombre: ")

    a = saludo()
    
    print(f"{a}{nom}")