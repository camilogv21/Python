#crear diccionarios===============================================================================


from cgi import print_directory


d1 = {
    "nombre" : "sara",
    "edad" : 27,
    "documento" : 123456789
}    


print(d1)
print("_"*50)
# o tambien se puede utilizar dict

d2 = dict([
    ("nombre" , "sara"),
    ("edad" , 27),
    ("documento" , 123456789)
])

print(d2)
print("_"*50)

#otra forma de utiliozar dict

d3 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789
)

print(d3)
print("="*50)

#leer diccionarios===================================================================================
# solo se leen las key
d4 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789
)

for a in d4:

    print(a)

print("_"*50)

#solo se leen los value

d5 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789
)

for a in d5:

    print(d5[a])

print("_"*50)

#se leen ambas

d6 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789
)

for a,b in d6.items():

    print(a,b)

print("="*50)

#acceder============================================================================================================

d7 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789
)

print(d7.get("nombre"))

print("="*50)

#modificar===========================================================================================================

d8 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789
)

d8["nombre"] = "laura"

print(d8)

print("_"*50)

#si el key no exixte se añade automaticamente

d9 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789
)

d9["direccion"] = 123


print(d9)

print("="*50)

#metodos asociados====================================================================================================

d10 = dict(
    nombre = "sara",
    edad = 27,
    documento = 123456789,
    direccion = 123
)


#metodo consultar get()

print(d10.get("nombre"))

print("_"*50)

#metodo items()

it = d10.items()

print(it)
print(list(it))

print("_"*50)

#metodo keys()

k = d10.keys()

print(k)
print(list(k))

print("_"*50)

# metodo values()

print(list(d10.values()))

print("_"*50)

#metodo pop()

d10.pop("direccion")

print(d10)
 
print("_"*50)

#metodo popitem()

d10.popitem()
print(d10)

print("_"*50)

# metodo update()

d102 = dict(
    nombre = "camilo",
    edad = 20,
    documento = 987654321,
    direccion = 321
)

d10.update(d102)

print (d10)

print("_"*50)

#metodo eliminar clear()

d10.clear()
print(d10)


print("="*50)

#diccionarios anidados================================================================================================
anidado1 = {"nombre" : "sara", "edad" : 27}
anidado2 = {"documento" : 123456789 , "direccion" : 123}

d11 = {
    "anidado_a" : anidado1,
    "anidado_b" : anidado2
}
 
print(d11)