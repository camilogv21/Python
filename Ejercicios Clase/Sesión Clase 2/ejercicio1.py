#Actividad 1. Usando POO.
"""
Escribir un programa que pida al usuario el número de gramos de masa de un camión (objeto).
Y usando varios métodos mostrar en pantalla las conversiones de dicha cantidad:
 - Kilogramos
 - Libras
 - Onzas
"""
class Camion:
    def __init__(self, peso):
        self.gramos = peso
        self.kg = 0
        self.lib = 0
        self.oz = 0
    def convertirKG(self):
        self.kg = self.gramos * 0.001
        return self.kg
    def convertirLB(self):
        self.lib = self.gramos * 0.00220462
        return self.lib
    def convertirOZ(self):
        self.oz = self.gramos * 0.035274
        return self.oz





if __name__ == "__main__":
    masa = float(input("Digite el peso del camión en gramos: "))

    C1 = Camion(masa)

    print(f"Peso del camión en KG: {C1.convertirKG():0.2f}")

    print(f"Peso del camión en LB: {C1.convertirLB():0.2f}")

    print(f"Peso del camión en OZ: {C1.convertirOZ():0.2f}")
