"""
Módulo de vista para productos.
Maneja la interfaz de usuario por consola.
"""


class ProductoView:
    """
    Vista que gestiona la presentación de datos al usuario.
    """
    
    @staticmethod
    def mostrar_menu():
        """
        Muestra el menú principal del sistema.
        """
        print("\n" + "="*50)
        print("    GESTOR DE PRODUCTOS - EdiCommer")
        print("="*50)
        print("1. Listar productos")
        print("2. Agregar producto")
        print("3. Editar producto")
        print("4. Eliminar producto")
        print("5. Consultar producto por ID")
        print("6. Salir")
        print("="*50)
    
    @staticmethod
    def listar_productos(productos):
        """
        Muestra la lista de productos en formato de tabla.
        
        Args:
            productos (list): Lista de productos
        """
        if not productos:
            print("\nNo hay productos registrados.")
            return
        
        print("\n" + "-"*80)
        print(f"{'ID':<5} {'Nombre':<25} {'Precio':<12} {'Categoría':<20} {'Stock':<10}")
        print("-"*80)
        
        for producto in productos:
            print(f"{producto['id']:<5} {producto['nombre']:<25} ${producto['precio']:<11.2f} {producto['categoria']:<20} {producto['stock']:<10}")
        
        print("-"*80)
        print(f"Total de productos: {len(productos)}")
    
    @staticmethod
    def mostrar_producto(producto):
        """
        Muestra los detalles de un producto individual.
        
        Args:
            producto (dict): Datos del producto
        """
        if not producto:
            print("\nProducto no encontrado.")
            return
        
        print("\n" + "-"*50)
        print("DETALLES DEL PRODUCTO")
        print("-"*50)
        print(f"ID:         {producto['id']}")
        print(f"Nombre:     {producto['nombre']}")
        print(f"Precio:     ${producto['precio']:.2f}")
        print(f"Categoría:  {producto['categoria']}")
        print(f"Stock:      {producto['stock']}")
        print("-"*50)
    
    @staticmethod
    def solicitar_datos_producto():
        """
        Solicita los datos de un producto al usuario.
        
        Returns:
            tuple: (nombre, precio, categoria, stock)
        """
        nombre = input("Nombre del producto: ").strip()
        precio = input("Precio: ").strip()
        categoria = input("Categoría: ").strip()
        stock = input("Stock: ").strip()
        
        return nombre, precio, categoria, stock
    
    @staticmethod
    def solicitar_id():
        """
        Solicita el ID de un producto al usuario.
        
        Returns:
            str: ID ingresado por el usuario
        """
        return input("Ingrese el ID del producto: ").strip()
    
    @staticmethod
    def mostrar_mensaje(mensaje, tipo="info"):
        """
        Muestra un mensaje al usuario.
        
        Args:
            mensaje (str): Mensaje a mostrar
            tipo (str): Tipo de mensaje ('info', 'error', 'exito')
        """
        if tipo == "error":
            print(f"\n❌ Error: {mensaje}")
        elif tipo == "exito":
            print(f"\n✅ {mensaje}")
        else:
            print(f"\nℹ️  {mensaje}")
    
    @staticmethod
    def limpiar_pantalla():
        """
        Limpia la pantalla de la consola.
        """
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

