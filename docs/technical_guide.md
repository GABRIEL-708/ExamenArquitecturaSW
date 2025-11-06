# Guía Técnica de EdiCommer Pro

## Arquitectura del Sistema

### Patrón MVC (Model-View-Controller)

El sistema implementa una arquitectura MVC clara y modular para la gestión de productos:

#### 🎯 Modelo (`model/`)
- Implementa el acceso a datos mediante MySQL
- Usa patrón Singleton para la conexión a base de datos
- Clases principales:
  - `DatabaseConnection`: Gestión de conexión MySQL
  - `ProductoModel`: Operaciones CRUD y consultas

```python
# Ejemplo de ProductoModel
def listar_todos(self, orden_por='nombre', direccion='ASC', filtros=None):
    """
    Obtiene todos los productos con opciones de ordenamiento y filtrado.
    """
    cursor = self.conn.cursor()
    query = 'SELECT * FROM productos WHERE 1=1'
    # ... implementación del método
```

#### 🎮 Controlador (`controller/`)
- Implementa la lógica de negocio
- Realiza validaciones de datos
- Coordina entre modelo y vista

```python
# Ejemplo de ProductoController
def agregar_producto(self, codigo_sku, nombre, descripcion, precio, categoria, ...):
    """
    Agrega un nuevo producto con validaciones completas.
    """
    if not codigo_sku.strip():
        return False, "El código SKU no puede estar vacío", None
    # ... más validaciones e implementación
```

#### 🖥️ Vista (`view/`)
- Interfaz de consola interactiva
- Menú de operaciones CRUD
- Formateo de datos para presentación

```python
# Ejemplo de ProductoView
@staticmethod
def listar_productos(productos):
    print("\n" + "-"*80)
    print(f"{'ID':<5} {'Nombre':<25} {'Precio':<12} {'Categoría':<20} {'Stock':<10}")
    # ... implementación del método
```

### Patrones de Diseño Implementados

#### 🔒 Singleton para Conexión a Base de Datos
Implementado en la clase `DatabaseConnection`:

```python
class DatabaseConnection:
    _instance = None
    _connection = None
    
    def __new__(cls):
        """Implementación del patrón Singleton"""
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
    def connect(self):
        """Conexión a MySQL en Clever Cloud"""
        config = {
            "host": "bsgru36cv5yhisoln20d-mysql.services.clever-cloud.com",
            "database": "bsgru36cv5yhisoln20d",
            # ... configuración de conexión
        }
```

Beneficios implementados:
- Una única conexión a la base de datos
- Gestión centralizada de la conexión MySQL
- Manejo de errores específicos de conexión

### Estructura de Base de Datos

#### Tabla de Productos
```sql
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_sku VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10,2) NOT NULL,
    precio_oferta DECIMAL(10,2),
    categoria VARCHAR(100) NOT NULL,
    subcategoria VARCHAR(100),
    marca VARCHAR(100),
    stock INT NOT NULL DEFAULT 0,
    stock_minimo INT DEFAULT 5,
    unidad_medida VARCHAR(20),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    estado ENUM('activo', 'descontinuado', 'en_oferta') DEFAULT 'activo'
)
```

### Funcionalidades Implementadas

#### 📊 Gestión de Productos
1. **Listar Productos**
   - Ordenamiento por campos
   - Filtros por categoría, marca, precio
   - Visualización en formato tabla

2. **Agregar Producto**
   - Validación completa de datos
   - Generación de SKU único
   - Control de duplicados

3. **Editar Producto**
   - Actualización de campos principales
   - Validaciones de datos
   - Verificación de existencia

4. **Eliminar Producto**
   - Eliminación segura
   - Verificación previa
   - Confirmación de operación

### 🔍 Funciones de Búsqueda Implementadas

#### Búsquedas Principales
```python
# Búsqueda por ID
def buscar_por_id(self, producto_id):
    cursor.execute('SELECT * FROM productos WHERE id = %s', (producto_id,))

# Búsqueda por SKU
def buscar_por_sku(self, sku):
    cursor.execute('SELECT * FROM productos WHERE codigo_sku = %s', (sku,))

# Búsqueda por nombre
def buscar_por_nombre(self, nombre):
    cursor.execute('SELECT * FROM productos WHERE nombre = %s', (nombre,))
```

#### Filtros y Ordenamiento
```python
def listar_todos(self, orden_por='nombre', direccion='ASC', filtros=None):
    # Filtros implementados:
    # - Categoría
    # - Rango de precios
    # - Stock bajo
    # - Productos en oferta
```

### ⚡ Características de Seguridad

#### Prepared Statements
- Prevención de SQL Injection
- Manejo seguro de parámetros
- Validación de tipos de datos

#### Validaciones Implementadas
```python
# Ejemplo de validaciones
if not codigo_sku.strip():
    return False, "El código SKU no puede estar vacío"
    
try:
    precio = float(precio)
    if precio < 0:
        return False, "El precio no puede ser negativo"
except ValueError:
    return False, "El precio debe ser un número válido"
```

## Validaciones Implementadas

### 🛡️ Validaciones de Productos

#### En el Controlador
```python
# Validaciones al agregar producto
def agregar_producto(self, codigo_sku, nombre, descripcion, precio, categoria, ...):
    # Campos requeridos
    if not codigo_sku.strip():
        return False, "El código SKU no puede estar vacío", None
    
    # Validación de precio
    try:
        precio = float(precio)
        if precio < 0:
            return False, "El precio no puede ser negativo", None
    except ValueError:
        return False, "El precio debe ser un número válido", None
    
    # Validación de stock
    try:
        stock = int(stock)
        if stock < 0:
            return False, "El stock no puede ser negativo", None
    except ValueError:
        return False, "El stock debe ser un número entero", None
```

### 🔒 Seguridad de Datos

#### Prevención de SQL Injection
```python
# Uso consistente de prepared statements
cursor.execute('SELECT * FROM productos WHERE id = %s', (producto_id,))
```

## Interfaz de Usuario

### 🖥️ Menú Principal
```
========================================
    GESTOR DE PRODUCTOS - EdiCommer
========================================
1. Listar productos
2. Agregar producto
3. Editar producto
4. Eliminar producto
5. Consultar producto por ID
6. Salir
========================================
```

### � Visualización de Productos
```
--------------------------------------------------------------------------------
ID    Nombre                     Precio       Categoría            Stock     
--------------------------------------------------------------------------------
1     Producto A                 $99.99       Electrónicos        50       
2     Producto B                 $149.99      Computación         25       
--------------------------------------------------------------------------------
```

## 🔄 Flujo de Operaciones

### Proceso de Creación
1. Usuario selecciona "Agregar producto"
2. Sistema solicita datos:
   - Nombre del producto
   - Precio
   - Categoría
   - Stock
3. Sistema valida datos
4. Se confirma la creación

### Proceso de Edición
1. Usuario selecciona "Editar producto"
2. Ingresa ID del producto
3. Sistema muestra datos actuales
4. Usuario ingresa nuevos datos
5. Sistema valida y actualiza

### Proceso de Eliminación
1. Usuario selecciona "Eliminar producto"
2. Ingresa ID del producto
3. Sistema confirma existencia
4. Se ejecuta eliminación
5. Se confirma operación

## 📊 Operaciones de Base de Datos

### Operaciones Principales
- Conexión segura a MySQL en Clever Cloud
- Creación automática de tablas
- Gestión de transacciones
- Manejo de errores de conexión

### Estructura de Datos
```sql
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    codigo_sku VARCHAR(50) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    stock INT NOT NULL DEFAULT 0
    -- ... otros campos implementados
)
```

## 📸 Capturas del Sistema

### 1. Inicio del Sistema
![Captura del sistema](../images/ejecucion%20python.png)
- Muestra la ejecución inicial del programa
- Interfaz principal del sistema

### 2. Gestión de Productos

#### Listado de Productos
![Captura del sistema](../images/listar%20productos.png)
- Vista completa del inventario
- Formato tabular con todos los productos

#### Agregar Producto
![Captura del sistema](../images/agregar%20nuevo%20producto.png)
- Proceso de creación de producto
- Formulario de ingreso de datos

#### Consulta por ID
![Captura del sistema](../images/Consultar%20por%20ID.png)
- Búsqueda de producto específico
- Visualización detallada

#### Edición de Producto
![Captura del sistema](../images/Editar%20producto.png)
![Captura del sistema](../images/Editar%20producto%202.png)
- Proceso de modificación
- Confirmación de cambios

#### Eliminación de Producto
![Captura del sistema](../images/Eliminar%20Producto.png)
- Proceso de eliminación
- Confirmación de seguridad

### 3. Resultados y Mensajes
![Captura del sistema](../images/Salida%20de%20la%20terminal%20.png)
- Mensajes del sistema
- Confirmaciones de operaciones