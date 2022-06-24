class Plumber:
    """
    Crea un fontanero
    """
    #atributo de clase, global para todos los objetos de esta clase
    character_type = 'plumber'

    def __init__(self, name):
        self.name = name
        self.__vidas = 5
        self._protegido = "todo"

    def jump(self):
        print(self.name, "jumps!")

    def movement(self, direction):
        print(self.name, "moves", direction)


class Villain:
    """
    Creates a villain
    """  


    character_type = 'villain'    
    
    def __init__(self, name):
        self.name = name    
        
    def jump(self):
        print(self.name, "jumps!")    
        
    def movement(self, direction):
        print(self.name, "moves", direction)



if __name__ == "__main__":
    
    player1 = Plumber('Mario')
    player2 = Plumber('Luigi')

    print(player1.name)
    print(player2.name)

    player1.jump()
    player2.movement('izquierda')

    print(player2.character_type)