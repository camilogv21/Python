class Tienda:
    
    def __init__(self, nombre, nit, dir, tel):
        self.nombre = nombre
        self.nit = nit
        self.dir = dir
        self.tel = tel
        self.estado = False
    
    def abrirTienda(self):
        self.estado = True
        print("Tienda abierta")
    
    def cerrarTienda(self):
        self.estado = False
        print("Tienda cerrada")

    def __str__(self) -> str:
        return f"Tienda: {self.nombre}"

if __name__ == "__main__":
    print(f"No soy un archivo principal")
