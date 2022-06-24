"""
Crear una clase cualquiera.
Llevar la cuenta de los objetos creados. ID (atributo de instancia)

En el main:
 - Preguntar al usuario cuántos objetos quiere Crear
 - Crearlos (instancias de camión)
 - Imprimir los Id de cada objeto.

"""
class Compu:
    """Clase para objetos tipo computador."""
    def __init__(self, cont):
        self.ID = cont

if __name__ == '__main__':
    n = int(input("Cuántos objetos quiere crear?: "))
    pc = []
    for i in range(1, n+1):
        computador = Compu(i)
        pc.append(computador)

    #operadores ternarios
    #list comprehensions python
    #[pc.append(Compu(i)) for i in range(1, n+1)]


    for x in pc:
        print(f"Objeto creado: {x.ID}")

    print(pc[0].ID)
    print(pc[1].ID)
