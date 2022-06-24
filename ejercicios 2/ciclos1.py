#ciclos:        for(para)         while(mientras)

# while   (bucle o ciclo mientras)

d = 0
while d <= 10:
    d += 1
    if d == 3:
        continue
    
    print(d)
    
    if d == 8 :
        break
else:
    print("El ciclo terminó correctamente")

letra = ""
while letra != "f":
    letra = input("Digite la letra secreta: ")


print("Adivinaste!!")
