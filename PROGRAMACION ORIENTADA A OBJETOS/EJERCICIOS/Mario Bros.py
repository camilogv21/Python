"""
def jump(jugador):
        print(jugador, "salta!")
        
def movement(jugador, direccion):
        print(jugador, "se desplaza a la", direccion)
        
def run_and_jump(jugador, direccion):
    movement(jugador, direccion)
    print("y")
    jump(jugador)
"""
"""
class Fontanero():
    
    crear un fontanero
    
        
    character_type = "fontanero"
    
    def __init__(self, jugador):
        self.jugador = jugador

    def jump(self):
        print(self.jugador, "salta!")
        
    def movement(self, direccion):
        print(self.jugador, "se desplaza a la", direccion)
        
class VilLano():
    
    crear villanos
    
    
    character_type = "villanos"  
    
    def __init__(self, villano):
        self.villano = villano

    def jump(self):
        print(self.villano, "salta!")
        
    def movement(self, direccion):
        print(self.villano, "se desplaza a la", direccion) 
    """
        
class Character():
           
    def __init__(self, jugador):
        self.jugador = jugador

    def jump(self):
        print(self.jugador, "salta!")
        
    def movement(self, direccion):
        print(self.jugador, "se desplaza a la", direccion)
        
class Fontanero(Character):
    """
    crear fontanero
    """
    character_type = "fontanero"
    
class Villano(Character):
    """
    crear villano
    """
    character_type = "villano"
    


if __name__=="__main__":
    
    """ 
- 1 Mario
- 1 Luigi
- 1 Princesa Peach
- 1 Bowser
- 100 Koopa Troopa
- 200 Goomba
- 50 Boo 
"""
    
    jugador1 = Fontanero ("Mario")
    jugador2 = Fontanero ("Luigi")
    enemigo1 = Villano ("Koopa Troopa")
    enemigo2 = Villano ("Goomba")
    
    """jump(jugador2)"""
    
    """movement(jugador1,"izquierda")"""
    
    """run_and_jump(jugador1,"derecha")"""
    
    print(jugador1.jugador)
    print(jugador1.character_type)
    jugador1.jump()
    jugador2.movement("izquierda")
    
    print(enemigo1.jugador)
    print(enemigo1.character_type)
    



