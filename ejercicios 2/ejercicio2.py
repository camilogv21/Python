#Pedir el estado del semáforo y decir un mensaje en caso.
#   upper()
#   lower()

semaforo = input("Digite el color del semáforo: ").lower()

if semaforo == "rojo":
    print(f"Estado: {semaforo.upper()} , pare!!" )
elif semaforo == "verde":
    print(f"Estado: {semaforo.upper()} , siga!!" )
elif semaforo == "amarillo":
    print(f"Estado: {semaforo.upper()} , precaución!!" )
else:
    print("Error")

