""" Adivina el personaje
Escriba un programa que pida al usuario elegir uno de los personajes de la lista
de abajo (sin informar su eleccion a su programa).

posteriormente, su programa debe hacer al usuario un conjunto de prguntas 
(maximo 5) dde tipo si/no hasta determinar  el personaje escogido por 
usuario.

personajes:
Radamel Falcao Garcia,goku,Michael Jordan,Eminem,Darth Vader Adam Sandler, 
Bruce Wayne, Tin Tin, Ayudante de santa, Joe Biden, Jose Saramago, Gunter Grass
y Kim Jong Un"""

class adivinar:
    
    def __init__(self):
        self.opcion = ""
        
    def preguntas(self):
        self.opcion = str(input("Su personaje es animado?: "))
        
        if self.opcion == "si":
            self.opcion = str(input("Su personaje tiene poderes?: "))
            if self.opcion == "si":
                print("Goku")
            else:
                self.opcion = str(input("Su personajes es un aventurero?: "))
                if self.opcion == "si":
                    print("Tin Tin")
                else:
                    print("Ayudante de santa")
        else:
            self.opcion = str(input("Su personaje es deportista?: "))
            if self.opcion == "si":
                self.opcion = str(input("Su personaje juega futbol?: "))
                if self.opcion == "si":
                    print("Radamel Falcao")
                else:
                    print("Michael Jordan")
            else:
                self.opcion = str(input("Su personaje ha actuando en alguna pelicula?: "))
                if self.opcion == "si":
                    self.opcion = str(input("Su personaje viste de negro?: "))
                    if self.opcion == "si":
                        self.opcion = str(input("Su personaje representa algun animal: "))
                        if self.opcion == "si":
                            print("Bruce Wayne")
                        else:
                            print("Darth Vader")
                    else:
                        print("Adam Sandler")
                else:
                    self.opcion = str(input("Su personaje ya murio?: "))
                    if self.opcion == "si":
                        self.opcion = str(input("Su personaje nacio en portugal?: "))
                        if self.opcion == "si":
                            print("Jose Saramago")
                        else:
                            print("Gunter Grass")
                    else:
                        self.opcion = str(input("Su personaje nacio en Estado Unidos?: "))
                        if self.opcion == "si":
                            self.opcion = str(input("Su personaje esta en la politica?: "))
                            if self.opcion == "si":
                                print("Joe Biden")
                            else:
                                print("Eminem")
                        else:
                            print("Kim Jong Un")
                    
if __name__ == "__main__":
    
    print("***Escoge un personajes*** \n\n ")
    print("1-Radamel Falcao \n"
          "2-Goku \n"
          "3-Michael Jordan \n"
          "4-Eminem \n"
          "5-Darth Vader \n" 
          "6-Adam Sandler \n" 
          "7-Bruce Wayne \n" 
          "8-Tin Tin \n" 
          "9-Ayudante de santa \n" 
          "10-Joe Biden \n" 
          "11-Jose Saramago \n" 
          "12-Gunter Grass \n" 
          "13-Kim Jong Un\n\n"
          "=====================\n\n")
        
    opc = adivinar()
    print(opc.preguntas())