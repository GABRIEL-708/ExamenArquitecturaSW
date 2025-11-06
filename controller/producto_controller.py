"""
Módulo de controlador para productos.
Maneja la lógica de negocio y coordina entre el modelo y la vista.
"""

from model.producto_model import ProductoModel


class ProductoController:
    """
    Controlador que gestiona la lógica de negocio para productos.
    """
    
    def __init__(self):
        """Inicializa el controlador con el modelo."""
        self.model = ProductoModel()
    
    def listar_productos(self):
        """
        Obtiene la lista de todos los productos.
        
        Returns:
            list: Lista de productos
        """
        return self.model.listar_todos()
    
    def obtener_producto(self, producto_id):
        """
        Obtiene un producto por su ID.
        
        Args:
            producto_id (int): ID del producto
            
        Returns:
            dict: Producto encontrado o None
        """
        try:
            producto_id = int(producto_id)
            return self.model.buscar_por_id(producto_id)
        except (ValueError, TypeError):
            return None
    
    def agregar_producto(self, nombre, precio, categoria, stock):
        """
        Agrega un nuevo producto con validaciones.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            categoria (str): Categoría del producto
            stock (int): Cantidad en stock
            
        Returns:
            tuple: (éxito: bool, mensaje: str, producto_id: int o None)
        """
        # Validaciones básicas
        nombre = nombre.strip() if nombre else ""
        categoria = categoria.strip() if categoria else ""
        
        # Validar campos requeridos
        if not nombre:
            return False, "El nombre no puede estar vacío", None
        
        if not categoria:
            return False, "La categoría no puede estar vacía", None
        
        # Validar precio
        try:
            precio = float(precio)
            if precio < 0:
                return False, "El precio no puede ser negativo", None
        except (ValueError, TypeError):
            return False, "El precio debe ser un número válido", None
        
        # Validar stock
        try:
            stock = int(stock)
            if stock < 0:
                return False, "El stock no puede ser negativo", None
        except (ValueError, TypeError):
            return False, "El stock debe ser un número entero válido", None
        
        # Verificar duplicado por nombre
        producto_existente = self.model.buscar_por_nombre(nombre)
        if producto_existente:
            return False, f"Ya existe un producto con el nombre '{nombre}'", None
        
        # Crear producto
        try:
            producto_id = self.model.crear(
                nombre=nombre,
                precio=precio,
                categoria=categoria,
                stock=stock
            )
            return True, f"Producto '{nombre}' agregado exitosamente", producto_id
        except Exception as e:
            return False, f"Error al agregar producto: {str(e)}", None
    
    def editar_producto(self, producto_id, nombre, precio, categoria, stock):
        """
        Edita un producto existente con validaciones.
        
        Args:
            producto_id (int): ID del producto a editar
            nombre (str): Nuevo nombre
            precio (float): Nuevo precio
            categoria (str): Nueva categoría
            stock (int): Nuevo stock
            
        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        # Convertir producto_id a entero para asegurar comparación correcta
        try:
            producto_id = int(producto_id)
        except (ValueError, TypeError):
            return False, "El ID debe ser un número válido"
        
        # Verificar que el producto existe
        producto = self.model.buscar_por_id(producto_id)
        if not producto:
            return False, f"No existe un producto con ID {producto_id}"
        
        # Validaciones (iguales que en agregar)
        nombre = nombre.strip() if nombre else ""
        categoria = categoria.strip() if categoria else ""
        
        if not nombre:
            return False, "El nombre no puede estar vacío"
        
        if not categoria:
            return False, "La categoría no puede estar vacía"
        
        try:
            precio = float(precio)
            if precio < 0:
                return False, "El precio no puede ser negativo"
        except (ValueError, TypeError):
            return False, "El precio debe ser un número válido"
        
        try:
            stock = int(stock)
            if stock <= 0:
                return False, "El stock debe ser mayor que 0"
        except (ValueError, TypeError):
            return False, "El stock debe ser un número entero válido"
        
        # Verificar duplicados (excepto el mismo producto)
        # Solo verificar si el nombre cambió respecto al original
        if nombre != producto['nombre']:
            producto_existente = self.model.buscar_por_nombre(nombre)
            if producto_existente and producto_existente['id'] != producto_id:
                return False, f"Ya existe otro producto con el nombre '{nombre}'"
        
        # Actualizar producto
        try:
            if self.model.actualizar(producto_id, nombre, precio, categoria, stock):
                return True, f"Producto '{nombre}' actualizado exitosamente"
            else:
                return False, "No se pudo actualizar el producto"
        except Exception as e:
            return False, f"Error al actualizar producto: {str(e)}"
    
    def eliminar_producto(self, producto_id):
        """
        Elimina un producto.
        
        Args:
            producto_id (int): ID del producto a eliminar
            
        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        try:
            producto_id = int(producto_id)
        except (ValueError, TypeError):
            return False, "El ID debe ser un número válido"
        
        producto = self.model.buscar_por_id(producto_id)
        if not producto:
            return False, f"No existe un producto con ID {producto_id}"
        
        try:
            if self.model.eliminar(producto_id):
                return True, f"Producto '{producto['nombre']}' eliminado exitosamente"
            else:
                return False, "No se pudo eliminar el producto"
        except Exception as e:
            return False, f"Error al eliminar producto: {str(e)}"

