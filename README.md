Trabajo Práctico Integrador (TPI) 2026
Programación Avanzada

Profesor Gianluca Piriz

Grupo : 
Integrantes : Maximo Barraza - Gabriel Ávila

- - - [Clases] - - -

[Producto] 
Clases hijas : (ProductoElectronico) ; (ProductoAlimenticio) ; (ProductoContstruccion)

Nuestro trabajo se basa en un Sistema de gestión de Inventario de Productos, Funciona en base una Clase principal la cual es 'Producto', esta recibe como parametros (id, nombre, precio, stock, proveedor), como definiciones (funciones) tiene a mostrar_informacion() y a calculo_impuestos(), tambien tiene clases hijas como ProductoElectronico(Producto), ProductoAlimenticio(Producto) y ProductoConstruccion(Producto).

[Inventory]
La Clase 'Inventory' almacena los objetos creados en una lista denominada 'productos', esta clase luego puede ser usada para acceder a los datos de los objetos almacenados como su id, nombre, precio, etc.

[Proveedor]
La Clase 'Proveedor' es un agregado a el objeto creado en 'ProductoFactory', se almacena en el parametro 'proveedor' y luego puede ser accedido mediante el menu.

[ProductoFactory]
La Clase 'ProductoFactory' Implementa el patrón de diseño Factory Method, se encarga de crear el tipo de producto correspondiente segun el dato ingresado por el usuario.

[Menu]
El menú es una función que es usada como interfaz para acceder a las diferentes funciones del programa, dentro del menu, mendiante códigos, el usuario puede acceder a las diferentes funcionalidades del programa, por ejemplo, agregar un producto, ver los productos almacenador, calcular los impuestos, etc.

[Conceptos Utilizados]
Encapsulamiento : Los datos de cada objeto se agrupan dentro de sus clases.
Abstracción : Cada Clase un objeto importante en el dominio.
Herencia : Los productos especificos heredan de la clase 'Producto'.
Polimorfismo : Cada tipo de producto calcula sus impuestos de manera diferente.
Asociación : Un producto se relaciona con un proveedor.
Agregación : El invetario contiene una lista de productos.

[Patrón de diseño]
Este sistema cuenta con el patrón de diseño de 'Factory Method' mediante la clase ProductoFactory(), ya que este programa proporciona una interfaz para la creación de objetos en una super clase, junto a otras clases que alteran la creación de estos objetos, por ejemplo, dentro de esta misma clase se aplican los impuestos usando las clases ProductoElectronico, ProductoAlimenticio o ProductoConstrucción.

[Funcionalidades]
* Agregar un producto
* Mostrar información de los productos almacenados
* Calcular impuestos de productos
* Calcular precio total de stock
