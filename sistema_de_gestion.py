class Producto():

    def __init__ (self, id, nombre, precio, stock, proveedor):

        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor

    def mostrar_informacion(self):

        print(
            f"\n Informacion del Producto ID[{self.id}]"
            f"\n Nombre : {self.nombre}"
            f"\n Precio : ${self.precio}"
            f"\n Impuesto : ${self.calculo_impuestos()}"
            f"\n Precio final : ${self.calculo_precio_final()}"
            f"\n Precio del Stock con Impuestos : ${self.calculo_precio_final_stock()}"
            f"\n Stock : {self.stock}"
            f"\n Proveedor : {self.proveedor.nombre} | Telefono : {self.proveedor.telefono}"
           
        )
        
    def calculo_impuestos(self):
        return 0
    
    def calculo_precio_final(self):
        return self.precio + self.calculo_impuestos()
    
    def calculo_precio_final_stock(self):
        return self.calculo_precio_final() * self.stock
    
class ProductoElectronico(Producto):

    def calculo_impuestos(self):
        return self.precio * 0.50
    
class ProductoAlimenticio(Producto):

    def calculo_impuestos(self):
        return self.precio * 0.22
    
class ProductoConstruccion(Producto):

    def calculo_impuestos(self):
        return self.precio * 0.35
        
class ProductoFactory():

    @staticmethod
    def crear_producto(tipo, id, nombre, precio, stock, proveedor):

        if (tipo == "electronico"):

            return ProductoElectronico(id, nombre, precio, stock, proveedor)
        
        elif (tipo == "alimenticio"):

            return ProductoAlimenticio(id, nombre, precio, stock, proveedor)
        
        elif (tipo == "construccion"):

            return ProductoConstruccion(id, nombre, precio, stock, proveedor)
        
        else:
            return Producto(id, nombre, precio, stock, proveedor)
    
class Inventario():

    def __init__(self):

        self.productos = []

    def buscar_producto(self, id_producto):

        for producto in self.productos:

            if producto.id == id_producto:

                return producto
            
        return None

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
        
        print("\nIngrese 'H' para ver la lista de comandos\n")
        id_comando = input("Ingrese el id del comando: ").lower()

        if (id_comando == "h"):

            print(
            "\n- Lista de Comandos - \n" \
            "\n [X] Terminar programa" \
            "\n [1] Agregar un producto" \
            "\n [2] Mostrar información de productos almacenados"
            "\n [3] Calcular impuestos de productos"
            "\n [4] Calcular precio total de stock"
            "\n [5] Buscar producto por id"
            )

        if (id_comando == "1"):

            print("\n- [Ingrese los datos del producto] -\n")

            tipo_producto = input("Ingrese tipo de producto : ").lower()
            id_producto = int(input("Ingrese Id : "))
            nombre_producto = input("Ingrese Nombre : ")
            precio_producto = int(input("Ingrese Precio : "))
            stock_producto = int(input("Ingrese Stock : "))
            proveedor = Proveedor(
                input("Ingrese nombre del proveedor : "),
                input("Ingrese el numero del proveedor : ")
            )

            producto = ProductoFactory.crear_producto(tipo_producto, id_producto, nombre_producto, precio_producto, stock_producto, proveedor)

            inventario.agregar_producto(producto)

        if (id_comando == "2"):

            if len(inventario.productos) == 0:

                print("\n - [No hay productos en el inventario] - ")

            inventario.mostrar_productos()

        if (id_comando == "3"):

            if len(inventario.productos) == 0:

                print("\n - [No hay productos en el inventario] - ")

            for producto in inventario.productos:

                print(
                    f"\nID [{producto.id}]"
                    f"\nProducto : {producto.nombre}"
                    f"\nPrecio individual : ${producto.precio}"
                    f"\nImpuesto : ${producto.calculo_impuestos()}"
                    )
                
        if (id_comando == "4"):

            if len(inventario.productos) == 0:

                print("\n - [No hay productos en el inventario] - ")

            for producto in inventario.productos:

                print(
                    f"\nID [{producto.id}]"
                    f"\nProducto : {producto.nombre}"
                    f"\nStock : {producto.stock}" 
                    f"\nPrecio individual : ${producto.precio}"
                    f"\nPrecio total : ${producto.precio * producto.stock}"
                    f"\nPrecio total con impuestos: ${producto.calculo_precio_final_stock()}"
                )

        if (id_comando == "5"):

            if len(inventario.productos) == 0 :

                print("\n - [No hay productos en el inventario] - ")

                continue

            id_busqueda = int(input("Ingrese el id del producto : "))

            producto = inventario.buscar_producto(id_busqueda)

            if producto:

                print("Producto encontrado:")
                producto.mostrar_informacion()

            else:

                print("\nNo se ha encontrado el producto")

menu()