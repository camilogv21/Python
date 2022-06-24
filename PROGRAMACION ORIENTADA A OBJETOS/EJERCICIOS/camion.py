""" 
Escribir un programa que pida la usuario el numero de gramos de masa de un camion (objecto).
Y usando varios metodos mostrar en patanla las conversiones de dicha cantidad.
Cantidad:
- kilogramos
- libras
- onzas
"""

class camion:
    
    def __init__(self,gramos):
        self.gramos = gramos
        self.kilogramo = 0.001
        self.libras = 0.0022
        self.onzas = 0.035
        
    def verKilogramos(self):
        
        self.kilogramo = self.gramos * self.kilogramo
        return self.kilogramo
        
    def verLibras(self):
        
        self.libras = self.gramos * self.libras
        return self.libras
        
    def verOnzas(self):
        
        self.onzas = self.gramos * self.onzas
        return self.onzas
                 
        
if __name__ == "__main__":
       
    masaGramos = float(input("digite la masa de un camion: "))
    peso = camion(masaGramos)
    
    print(f"el peso del camion en kilogramos es: {peso.verKilogramos()}")
    print(f"el peso del camion en libras es: {peso.verLibras()}")
    print(f"el peso del camion en onzas es: {peso.verOnzas()}")
    
    
    
    
    
    
    
    
    
    
    
    
        
    
        
    