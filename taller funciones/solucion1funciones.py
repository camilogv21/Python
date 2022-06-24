"""1. Construir un script que le pida al usuario la cantidad, precio unitario de un producto y que haciendo
    uso de una función calcule el precio neto a pagar. Imprimir en la zona del algoritmo."""


def total(cantidad,precio):
    neto = (cantidad * precio)
    return neto
    

if __name__ == "__main__":

    cant = int(input("cantidad del producto: "))
    prec = int(input("precio unitario del preducto: "))

    net = total (cant,prec)

    print(f"el precio neto a paga es: {net}")
