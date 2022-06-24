class Character():
    """
    Creates a game character
    """    
    def __init__(self, name):
        self.name = name    
        
    def jump(self):
        print(self.name, "jumps!")    
        
    def movement(self, direction):
        print(self.name, "moves", direction)

class Plumber(Character):
    """
    Creates a plumber
    """
    character_type = 'plumber'



class Villain(Character):
    """
    Creates a villain
    """    
    character_type = 'villain'    
    

class Princess(Character):
    """
    Creates a princess
    """
    character_type = 'princess'


class CarnivorousPlant(Character):
    """
    Creates a carvivorous plant
    """
    character_type = 'carnivorous plant'    
    
    def jump(self): 
        pass    
        
    def movement(self, direction): 
        pass

if __name__ == "__main__":
    
    #creación de objetos
    player1 = Plumber('Mario')
    player2 = Plumber('Luigi')

    #acceso a atributos de instancia
    print(player1.name)
    print(player2.name)

    #creación de objetos
    player3 = Villain('Wario')

    #acceso a atributos de clase
    print(player3.character_type)

    #creación de objetos
    player4 = Princess('Peach')
    player4.jump()

    #un objeto pertenece a una clase determinada
    print(isinstance(player4, Character))

    # ver los atributos y funciones de un objeto
    todo = dir(player4)
    print(todo)

    player4.movement()

    for i in todo:
        print(i)

    
    #creación de objetos
    plant = CarnivorousPlant('Generic Plant')
    plant.movement('izquierda')