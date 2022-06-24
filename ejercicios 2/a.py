numero = "0011092"

lst = []
for num in numero:
    if num == "0":
        lst.append("x")
    else:
        lst.append(num)

print(f"Esta es la lista con los cambios {lst}")

#convertir a un string

nuevo_num = ""
for i in lst:
    nuevo_num += i

print(f"Este el vector convertido a string {nuevo_num}")