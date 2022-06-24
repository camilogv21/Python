from tienda import *

class Producto:
    
    def __init__(self, id, nombre, codproducto, precio, cantidad, categoria, nombreT, nit, dir, tel):
        nombre, codproducto, precio, cantidad
        self.id = id
        self.nombre = nombre
        self.codproducto = codproducto
        self.precio = precio
        self.cantidad = cantidad
        
        self.tienda = Tienda(nombreT, nit, dir, tel)
        self.categoria = categoria
        
    
    def cambiarPrecio(self, precio:float):
        if precio >= 5000:
            self.precio = precio
            return "OK"
        else:
            return "No se pudo cambiar el precio"
        
    def verDetalles(self):
        print(
            f"""Los datos del producto son:
            ID: {self.id} 
            Nombre: {self.nombre} 
            COD: {self.codproducto} 
            Precio: {self.precio} 
            Cantidad: {self.cantidad} 
            Tienda: {self.tienda}
            """
        )

    def __str__(self) -> str:
        return f"Producto {self.nombre}"

if __name__ == "__main__":
    print(f"No soy un archivo principal")
