"""
Módulo de modelo para la entidad Producto.
Maneja el acceso a los datos de productos en la base de datos.
"""

from model.database import DatabaseConnection


class ProductoModel:
    """
    Modelo que gestiona las operaciones de base de datos para productos.
    """
    
    def __init__(self):
        db = DatabaseConnection()
        self.conn = db.get_connection()
    
    def _row_to_dict(self, columns, row):
        """
        Convierte una fila de resultados en un diccionario.
        
        Args:
            columns (list): Lista de nombres de columnas
            row (tuple): Fila de resultados
            
        Returns:
            dict: Diccionario con los datos de la fila
        """
        if not row:
            return None
        return dict(zip(columns, row))
    
    def listar_todos(self, orden_por='nombre', direccion='ASC', filtros=None):
        """
        Obtiene todos los productos de la base de datos con opciones de ordenamiento y filtrado.
        
        Args:
            orden_por (str): Campo por el cual ordenar ('nombre', 'precio', 'stock', etc.)
            direccion (str): Dirección del ordenamiento ('ASC' o 'DESC')
            filtros (dict): Diccionario con filtros a aplicar
                {
                    'categoria': str,
                    'marca': str,
                    'precio_min': float,
                    'precio_max': float,
                    'stock_bajo': bool,
                    'en_oferta': bool
                }
        
        Returns:
            list: Lista de diccionarios con los productos
        """
        cursor = self.conn.cursor()
        
        # Construir la consulta base
        query = 'SELECT * FROM productos WHERE 1=1'
        params = []
        
        # Aplicar filtros si existen
        if filtros:
            if 'categoria' in filtros and filtros['categoria']:
                query += ' AND categoria = %s'
                params.append(filtros['categoria'])
            
            if 'marca' in filtros and filtros['marca']:
                query += ' AND marca = %s'
                params.append(filtros['marca'])
            
            if 'precio_min' in filtros and filtros['precio_min'] is not None:
                query += ' AND precio >= %s'
                params.append(float(filtros['precio_min']))
            
            if 'precio_max' in filtros and filtros['precio_max'] is not None:
                query += ' AND precio <= %s'
                params.append(float(filtros['precio_max']))
            
            if 'stock_bajo' in filtros and filtros['stock_bajo']:
                query += ' AND stock <= stock_minimo'
            
            if 'en_oferta' in filtros and filtros['en_oferta']:
                query += ' AND precio_oferta IS NOT NULL'
        
        # Validar y aplicar ordenamiento
        campos_validos = ['id', 'nombre', 'precio', 'categoria', 'stock', 'marca', 'ultima_actualizacion']
        if orden_por not in campos_validos:
            orden_por = 'nombre'
        
        direccion = 'ASC' if direccion.upper() not in ['ASC', 'DESC'] else direccion.upper()
        
        query += f' ORDER BY {orden_por} {direccion}'
        
        # Ejecutar consulta
        cursor.execute(query, params)
        columns = [desc[0] for desc in cursor.description]
        productos = cursor.fetchall()
        return [self._row_to_dict(columns, producto) for producto in productos]
        
    def buscar_por_sku(self, sku):
        """
        Busca un producto por su SKU.
        
        Args:
            sku (str): Código SKU del producto
            
        Returns:
            dict: Datos del producto o None si no existe
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM productos WHERE codigo_sku = %s', (sku,))
        columns = [desc[0] for desc in cursor.description]
        producto = cursor.fetchone()
        return self._row_to_dict(columns, producto)
        
    def buscar_por_categoria(self, categoria):
        """
        Busca productos por categoría.
        
        Args:
            categoria (str): Categoría a buscar
            
        Returns:
            list: Lista de productos en esa categoría
        """
        return self.listar_todos(filtros={'categoria': categoria})
        
    def obtener_productos_stock_bajo(self):
        """
        Obtiene productos con stock bajo (menor o igual al mínimo).
        
        Returns:
            list: Lista de productos con stock bajo
        """
        return self.listar_todos(filtros={'stock_bajo': True})
        
    def obtener_productos_en_oferta(self):
        """
        Obtiene productos en oferta.
        
        Returns:
            list: Lista de productos en oferta
        """
        return self.listar_todos(filtros={'en_oferta': True})
    
    def buscar_por_id(self, producto_id):
        """
        Busca un producto por su ID.
        
        Args:
            producto_id (int): ID del producto
            
        Returns:
            dict: Datos del producto o None si no existe
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM productos WHERE id = %s', (producto_id,))
        columns = [desc[0] for desc in cursor.description]
        producto = cursor.fetchone()
        return self._row_to_dict(columns, producto)
    
    def buscar_por_nombre(self, nombre):
        """
        Busca un producto por su nombre.
        
        Args:
            nombre (str): Nombre del producto
            
        Returns:
            dict: Datos del producto o None si no existe
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM productos WHERE nombre = %s', (nombre,))
        columns = [desc[0] for desc in cursor.description]
        producto = cursor.fetchone()
        return self._row_to_dict(columns, producto)
    
    def crear(self, nombre, precio, categoria, stock=0):
        """
        Crea un nuevo producto en la base de datos.
        
        Args:
            nombre (str): Nombre del producto
            precio (float): Precio del producto
            categoria (str): Categoría del producto
            stock (int): Cantidad en stock
            
        Returns:
            int: ID del producto creado
        """
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO productos (
                nombre, precio, categoria, stock
            ) VALUES (
                %s, %s, %s, %s
            )
        ''', (
            nombre, precio, categoria, stock
        ))
        self.conn.commit()
        return cursor.lastrowid
    
    def actualizar(self, producto_id, nombre, precio, categoria, stock):
        """
        Actualiza un producto existente.
        
        Args:
            producto_id (int): ID del producto a actualizar
            nombre (str): Nuevo nombre
            precio (float): Nuevo precio
            categoria (str): Nueva categoría
            stock (int): Nuevo stock
            
        Returns:
            bool: True si se actualizó correctamente, False si no existe
        """
        cursor = self.conn.cursor()
        cursor.execute(
            'UPDATE productos SET nombre = %s, precio = %s, categoria = %s, stock = %s WHERE id = %s',
            (nombre, precio, categoria, stock, producto_id)
        )
        self.conn.commit()
        return cursor.rowcount > 0
    
    def eliminar(self, producto_id):
        """
        Elimina un producto de la base de datos.
        
        Args:
            producto_id (int): ID del producto a eliminar
            
        Returns:
            bool: True si se eliminó correctamente, False si no existe
        """
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM productos WHERE id = %s', (producto_id,))
        self.conn.commit()
        return cursor.rowcount > 0

