class Cliente:
    
    def __init__(self, nombre, cant_dinero):
        self.nombre = nombre
        self.cant_dinero = cant_dinero
        
        self.productos_comprados = []
    
    #                           obj
    def comprarProducto(self, producto):
        if producto.cantidad > 1:
            if self.cant_dinero > producto.precio:
                self.productos_comprados.append(producto)
                return "Producto comprado correctamente"
            else:
                return "No hay suficiente dinero"
        else:
            return "No hay stock"
        
    
    def verDetalles(self):
        total  = 0
        for i in self.productos_comprados:
            total += i.precio
            print(i)
        print(f"Total: ${total}")

    def __str__(self) -> str:
        return f"Cliente: {self.nombre}"

if __name__ == "__main__":
    print(f"No soy un archivo principal")
