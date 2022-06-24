class Cliente(object):
    def __init__(self):
        self.nombre = "Evelyn"
        self.apellido = "Rendón"
        self.__edad = 15

    def __str__(self):
        return f"Me llamo {self.nombre} edad {self.__edad}"


if __name__ == "__main__":
    cliente1 = Cliente()
    cliente1.nombre = "Jorge"
    print(cliente1)
