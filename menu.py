### Menu de comandos
from sistema_de_gestion import ProductoFactory, Inventario

def menu():

    inventario = Inventario()
    id_comando = ""

    while (id_comando.lower() != "x") :

        print(
            "- Lista de Comandos" \
            "\n [X] Terminar comando" \
            "\n [1] Agregar un producto" \
            "\n [2] Mostrar infomación del producto"
            )
        
        id_comando = input("Ingresa el id del comando: ")

        if (id_comando == "1"):

            print("[Ingrese los datos del producto]")

            id_producto = int(input("Ingrese Id : "))
            nombre_producto = input("Ingrese Nombre : ")
            precio_producto = int(input("Inprese Precio : "))
            stock_producto = int(input("Ingrese Stock : "))
            proveedor_producto = input("Ingrese Proveedor : ")

            producto = ProductoFactory.crear_producto(id_producto, nombre_producto, precio_producto, stock_producto, proveedor_producto)

            inventario.agregar_producto(producto)

        if (id_comando == "2"):

            producto.mostrar_informacion