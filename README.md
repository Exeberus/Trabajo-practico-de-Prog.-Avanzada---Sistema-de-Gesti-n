Trabajo Práctico Integrador (TPI) 2026
Programación Avanzada

Profesor Gianluca Piriz

Grupo : 
Integrantes : Maximo Barraza - Gabriel Ávila

[Clases]

Nuestro trabajo se basa en un Sistema de gestión de Inventario de Productos, Funciona en base 1 Clase principal la cual es 'Producto', esta recibe como parametros (id, nombre, precio, stock, proveedor), como definiciones (funciones) tiene a mostrar_informacion() y a calculo_impuestos(), tambien tiene clases hijas como ProductoElectronico(Producto), ProductoAlimenticio(Producto) y ProductoConstruccion(Producto).

Este sistema cuenta con el patrón de diseño de 'Factory Method', ya que este programa proporciona una interfaz para la creación de objetos en una super clase, junto a otras clases que alteran la creación de estos objetos, por ejemplo, dentro de esta misma clase se aplican los impuestos usando las clases ProductoElectronico, ProductoAlimenticio o ProductoConstrucción.

La Clase 'Inventory' almacena los objetos creados en una lista denominada 'productos', esta clase luego puede ser usada para acceder a los datos de los objetos almacenados como su id, nombre, precio, etc.

La Clase 'Proveedor' es un agregado a el objeto creado en 'ProductoFactory', se almacena en el parametro 'proveedor' y luego puede ser accedido mediante el menu.

[Menu]
El menú es una función que es usada como interfaz para acceder a las diferentes funciones del programa, dentro del menu, mendiante códigos, el usuario puede acceder a las diferentes funcionalidades del programa, por ejemplo, agregar un producto, ver los productos almacenador, calcular los impuestos, etc.
