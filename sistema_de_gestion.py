class Producto(): ## Primera clase

    def __init__ (self, id, nombre, precio, stock, proveedor): ## init para crear el producto

        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def mostrar_informacion(self):

        print(
            f"\n Informacion del Producto ID[{self.id}]"
            f"\n Nombre : {self.nombre}"
            f"\n Precio : {self.precio}"
            f"\n Stock : {self.stock}"
            f"\n Proveedor : {self.proveedor}"
        )
        
    def calculo_impuestos(self):
        return 0
    
class ProductoElectronico(Producto):

    def calculo_impuestos(self):
        return self.precio * 0.50
    
class ProductoAlimenticio(Producto):

    def calculo_impuestos(self):
        return self.precio * 0.22
        
class ProductoFactory():

    @staticmethod
    def crear_producto(tipo, id, nombre, precio, stock, proveedor):

        if (tipo == "electronico"):

            return ProductoElectronico(id, nombre, precio, stock, proveedor)
        
        elif (tipo == "alimenticio"):

            return ProductoAlimenticio(id, nombre, precio, stock, proveedor)
        
        else:
            return Producto(id, nombre, precio, stock, proveedor)
    
class Inventario():

    def __init__(self):

        self.productos = []

    def agregar_producto(self, producto):

        self.productos.append(producto)
        print("Se ha agregado el producto exitosamente")

    def mostrar_productos(self):

        if not self.productos:

            print("\n Error : No hay productos \n")
            return
        
        for producto in self.productos:
            
            producto.mostrar_informacion()

class Proveedor:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def menu():

    inventario = Inventario()
    id_comando = ""

    while (id_comando != "x") :
        
        print("\n Ingrese 'H' para ver la lista de comandos")
        id_comando = input("Ingresa el id del comando: ").lower()

        if (id_comando == "h"):

            print(
            "- Lista de Comandos - \n" \
            "\n [X] Terminar comando" \
            "\n [1] Agregar un producto" \
            "\n [2] Mostrar infomación de productos almacenados"
            "\n [3] Calcular impuestos de productos"
            )

        if (id_comando == "1"):

            print("[Ingrese los datos del producto]")

            tipo_producto = input("Ingrese tipo de producto : ").lower()
            id_producto = int(input("Ingrese Id : "))
            nombre_producto = input("Ingrese Nombre : ")
            precio_producto = int(input("Ingrese Precio : "))
            stock_producto = int(input("Ingrese Stock : "))
            proveedor_producto = input("Ingrese Proveedor : ")

            producto = ProductoFactory.crear_producto(tipo_producto, id_producto, nombre_producto, precio_producto, stock_producto, proveedor_producto)

            inventario.agregar_producto(producto)

        if (id_comando == "2"):

            inventario.mostrar_productos()

menu()