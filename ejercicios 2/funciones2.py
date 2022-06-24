# Funciones + Ciclos
def divi(num1, num2):
    if num2 != 0:
        return num1 / num2

if __name__ == "__main__":
    v = []
    for i in range(5):
        a = int(input("Digite un número: "))
        b = int(input("Digite un número: "))
        r = divi(a, b)
        if r == None:
            print(f"El resultado de dividir {a}/{b} es No definido")    
        else:
            print(f"El resultado de dividir {a}/{b} es: {r:0.2f}")

#   Tarea: Guardar los cálculos correcto en una LISTA y....
#   mostrar el tamaño de la LISTA y sus datos.