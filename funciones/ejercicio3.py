#ejercicio3: construir un conversor de moneda a dolares a pesos y viceversa.
#           pedir TRM (acuanto esta el dolar) y el dinero que tengo para convertir
#           nota: debe crear dos funciones.

def dolares(pesos,m):
    r = (m * pesos )
    return r
def pesos(pesos,dolares):
    a = (dolares * pesos)
    return a

if __name__ =="__main__":

    m = 0.00025
    d = int(input("a cuanto esta el dolar: "))
    x = input("cual quieres convertir: \n"
                   "1-dolar a pesos \n"
                   "2-pesos a dolares\n")
    p = int(input("que cantidad quiere convertir: "))

y = pesos(d,p)
z = dolares(m,p)

if x == 1 or "dolar a pesos":
    print(f"{p} dolares en pesos es: {y} pesos")

if x == 2 or "pesos a dolares":
    print(f"{p} pesos en dolares es {z} dolares")
