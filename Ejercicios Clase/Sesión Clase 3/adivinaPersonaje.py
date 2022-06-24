class Magia:
    def __init__(self):
        self.personaje = ""
    
    def adivinar(self):
        print("Escoja un personaje de la lista y momorícelo (no lo mencione):")
        print("1. Radamel Falcao García")	#deportista
        print("2. Goku")					#Dibujo animado o ficticio
        print("3. Michael Jordan")			#deportista
        print("4. Eminem")					#cantante
        print("5. Darth Vader")				#Dibujo animado o ficticio
        print("6. Adam Sandler")			#actor
        print("7. Bruce Wayne")				#actor
        print("8. Tin Tin")					#Dibujo animado o ficticio
        print("9. Ayudante de Santa")		#Dibujo animado o ficticio
        print("10. Joe Biden")				#político	
        print("11. José Saramago")			#escritor
        print("12. Günter Grass")			#escritor
        print("13. Kim Jong Un.")			#político
        
        print("Su personaje es un Dibujo animado o ficticio?: Responda SI/NO")
        opt = input()
        if opt == "SI":
            #print("2, 5, 8, 9")
            print("Su personaje usa casco?: Responda SI/NO")
            opt = input()
            if opt == "SI":
                self.personaje = "5. Darth Vader"
            else:
                print("Su personaje es un animal?: Responda SI/NO")
                opt = input()
                if opt == "SI":
                    self.personaje = "9. Ayudante de Santa"
                else:
                    print("Su personaje tiene un perro?: Responda SI/NO")
                    opt = input()
                    if opt == "SI":
                        self.personaje = "8. Tin Tin"
                    else:
                        self.personaje = "2. Goku"
                        
        else:
            print("Su personaje es político?: Responda SI/NO")
            opt = input()
            if opt == "SI":
                #print("10, 13")
                print("Su personaje es o fue un presidente de un país?: Responda SI/NO")
                opt = input()
                if opt == "SI":
                    self.personaje = "10. Joe Biden"
                else:
                    self.personaje = "13. Kim Jong Un."
            else:
                print("Su personaje es deportista?: Responda SI/NO")
                opt = input()
                if opt == "SI":
                    #print("1, 3")
                    print("Su personaje es juega con la mano?: Responda SI/NO")
                    opt = input()
                    if opt == "SI":
                        self.personaje = "3. Michael Jordan"
                    else:
                        self.personaje = "1. Radamel Falcao García"
                else:
                    print("Su personaje es actor?: Responda SI/NO")
                    opt = input()
                    if opt == "SI":
                        #print("6, 7")
                        print("Su personaje usa máscara?: Responda SI/NO")
                        opt = input()
                        if opt == "SI":
                            self.personaje = "7. Bruce Wayne"
                        else:
                            self.personaje = "6. Adam Sandler"
                    else:
                        print("Su personaje es cantante?: Responda SI/NO")
                        opt = input()
                        if opt == "SI":
                            #print("4")
                            self.personaje = "4. Eminem"
                        else:
                            self.personaje = None

        return self.personaje
     

if __name__ == "__main__":
    obj = Magia()
    
    print(f"Su personaje es {obj.adivinar()}")
    