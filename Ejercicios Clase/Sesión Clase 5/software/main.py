import config
import tienda
import producto
import cliente

if __name__ == "__main__":
    
    tp = tienda.Tienda("Principal", 1, "Centro", "20")
    print(tp)
    
    p1 = producto.Producto(0, "zapato", 25, 1000, 5, "producto", "Sede1", 45, "centro", "44")
    p2 = producto.Producto(1, "chanclas", 25, 2000, 5, "producto", "Sede2", 45, "centro", "44")
    p3 = producto.Producto(2, "guayos", 25, 3000, 0, "producto", "Sede3", 45, "centro", "44")
    
    lista_productos = []
    
    lista_productos.append(p1)
    lista_productos.append(p2)
    lista_productos.append(p3)
    
    c1 = cliente.Cliente("Ramiro", 10000)
    
    while True:
        a = input("Quiere abrir la tienda: SI / NO: ")
        if a.upper() == "SI":
            tp.abrirTienda()
            break
        elif tp.estado == False and a.upper() == "NO":
            tp.cerrarTienda()
            break
        else:
            print("No se hizo nada")
    
    
    while True:
        opt = int(input(
            """
            Que desea realizar:
            1. Ver productos
            2. Cambiar precio a producto
            3. Ver detalles de 1 producto
            4. Comprar producto
            5. Ver detalles del cliente
            6. Salir
            """
        ))
        
    
        if opt ==  1:
            print(p1, p2, p3, sep="\n")
            
        elif opt ==  2:

            cual = int(input(f"Elija el producto:\n \
                {lista_productos[0].id}. {lista_productos[0].nombre}\n \
                {lista_productos[1].id}. {lista_productos[1].nombre}\n \
                {lista_productos[2].id}. {lista_productos[2].nombre}\n \
                "
            ))
            
            precio = float(input(f"Digite el precio para el producto '{lista_productos[cual].nombre}' precio actual ${lista_productos[cual].precio}: "))
            
            print(lista_productos[cual].cambiarPrecio(precio))
            
        elif opt ==  3:
            
            cual = int(input(f"Elija el producto:\n \
                {lista_productos[0].id}. {lista_productos[0].nombre}\n \
                {lista_productos[1].id}. {lista_productos[1].nombre}\n \
                {lista_productos[2].id}. {lista_productos[2].nombre}\n \
                "
            ))

            lista_productos[cual].verDetalles()
            
        elif opt ==  4:
            cual = int(input(f"Elija el producto:\n \
                {lista_productos[0].id}. {lista_productos[0].nombre}\n \
                {lista_productos[1].id}. {lista_productos[1].nombre}\n \
                {lista_productos[2].id}. {lista_productos[2].nombre}\n \
                "
            ))
            
            print( c1.comprarProducto(lista_productos[cual]) )
            
        elif opt ==  5:
            c1.verDetalles()
            
        elif opt ==  6:
            break