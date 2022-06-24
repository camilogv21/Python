class Cliente:
    def __init__(self):
        self.nombre = "Evelyn"
        self.apellido = "Rendón"
        self.__edad = 15

    def verEdad(self):
        return self.__edad

    def editarEdad(self, edad):
        if edad > 5:
            self.__edad = edad
            return True
        return False

if __name__ == "__main__":
    cliente1 = Cliente()
    cliente1.nombre = "Jorge"
    print(cliente1.nombre)
    print( cliente1.verEdad() )

    e = int(input("Digite su edad: "))

    if cliente1.editarEdad(e):
        print("Todo ok")
    else:
        print("Error de edad")

    print( cliente1.verEdad() )
