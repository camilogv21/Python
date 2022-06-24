import random


class Character():
           
    def __init__(self,vida,ataque):
        self.vida = vida
        self.ataque = ataque

class Pikachu(Character):
    """
    crear a pikachu
    """
    character_type = "pikachu vida = 100  ataque = 55"
    
class Jigglypuff(Character):
    """
    crear a jigglypuff
    """
    character_type = "pikachu vida = 100  ataque = 45"
    

if __name__=="__main__":
    
    pikachu = Pikachu(100,55)
    jigglypuff = Jigglypuff(100,45)
    turno = random.randint(1,2)
    
    while pikachu.vida > 0 and jigglypuff.vida > 0:
        
        if turno == 1:
            print("El turno es de pikachu")
            jigglypuff.vida = jigglypuff.vida - pikachu.ataque  
            turno = 2
        else:
            print("El turno es de jigglypuff")
            pikachu.vida = pikachu.vida - jigglypuff.ataque
            turno = 1
        
    
    if pikachu.vida > 0:
        print("pikachu es el campeon")
    else:
        print("jigglypuff es el campeon")
        
    print(f"pikachu termino con {pikachu.vida} de vida")
    print(f"jigglypuff termino con {jigglypuff.vida} de vida")
            
    
    
    
    
