"""perdir el estado de un semaforo y dar un mensaje en caso:

"""



semaforo = input("en que estado esta el semaforo? ")

b = semaforo.lower()

if b == "verde":
    print ("puedes seguir...")
elif b == "amarillo":
    print ("redusca la velocidad...")
elif b == "rojo":
    print ("pare, no puede seguir...")
else:
    print("error")