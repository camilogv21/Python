from typing_extensions import Self


class cliente:
     
     def __init__(self):
          self.nombre = "camilo"
          self.apellidos = "galeano"
          self.__edad = 21
          
     def __str__(self):
          return "clientes"
          
     def VerEdad (self):
          return self.__edad
     
     def EditarEdad (self, edad):
          """ modificar la clase """
          if edad > 5:
               self.__edad = edad
               return True
          return False


if __name__ == "__main__":
    cliente1 = cliente()
    cliente1.nombre = "jorge"
    print(cliente1.nombre)
    print(cliente1.VerEdad())