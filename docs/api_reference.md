# Referencia de Funciones - EdiCommer Pro

## 🔄 Funciones Principales

### Gestión de Productos

#### Listar Productos
```python
def listar_productos(self):
    """
    Obtiene la lista de todos los productos.
    
    Returns:
        list: Lista de productos con sus detalles
    """
```

**Ejemplo de Respuesta**
```python
[
    {
        "id": 1,
        "nombre": "Producto 1",
        "precio": 100.00,
        "categoria": "Categoría A",
        "stock": 50
    }
]
```

#### Obtener Producto por ID
```python
def obtener_producto(self, producto_id):
    """
    Obtiene un producto específico por su ID.
    
    Args:
        producto_id (int): ID del producto a buscar
        
    Returns:
        dict: Datos del producto o None si no existe
    """
```

**Ejemplo de Respuesta**
```python
{
    "id": 1,
    "nombre": "Producto 1",
    "precio": 100.00,
    "categoria": "Categoría A",
    "stock": 50
}
```
```

#### Agregar Producto
```python
def agregar_producto(self, nombre, precio, categoria, stock):
    """
    Agrega un nuevo producto al sistema.
    
    Args:
        nombre (str): Nombre del producto
        precio (float): Precio del producto
        categoria (str): Categoría del producto
        stock (int): Cantidad en stock
        
    Returns:
        tuple: (éxito: bool, mensaje: str, producto_id: int)
    """
```

**Ejemplo de Uso**
```python
exito, mensaje, producto_id = controller.agregar_producto(
    nombre="Producto Nuevo",
    precio=150.00,
    categoria="Categoría A",
    stock=100
)
```

**Ejemplo de Respuesta**
```python
(True, "Producto 'Producto Nuevo' agregado exitosamente", 1)
```
```

#### Editar Producto
```python
def editar_producto(self, producto_id, nombre, precio, categoria, stock):
    """
    Edita un producto existente.
    
    Args:
        producto_id (int): ID del producto a editar
        nombre (str): Nuevo nombre
        precio (float): Nuevo precio
        categoria (str): Nueva categoría
        stock (int): Nuevo stock
        
    Returns:
        tuple: (éxito: bool, mensaje: str)
    """
```

**Ejemplo de Uso**
```python
exito, mensaje = controller.editar_producto(
    producto_id=1,
    nombre="Producto Actualizado",
    precio=200.00,
    categoria="Categoría B",
    stock=75
)
```

**Ejemplo de Respuesta**
```python
(True, "Producto 'Producto Actualizado' actualizado exitosamente")
```
```

#### Eliminar Producto
```python
def eliminar_producto(self, producto_id):
    """
    Elimina un producto del sistema.
    
    Args:
        producto_id (int): ID del producto a eliminar
        
    Returns:
        tuple: (éxito: bool, mensaje: str)
    """
```

**Ejemplo de Uso**
```python
exito, mensaje = controller.eliminar_producto(producto_id=1)
```

**Ejemplo de Respuesta**
```python
(True, "Producto 'Nombre del Producto' eliminado exitosamente")
```
```

## 🚦 Códigos de Estado

| Código | Descripción                                          |
|--------|-----------------------------------------------------|
| 200    | OK - La solicitud se completó exitosamente          |
| 201    | Created - Recurso creado exitosamente               |
| 400    | Bad Request - Solicitud inválida                    |
| 401    | Unauthorized - No autorizado                        |
| 403    | Forbidden - Acceso prohibido                        |
| 404    | Not Found - Recurso no encontrado                   |
| 500    | Internal Server Error - Error interno del servidor  |

## 🔒 Autenticación

### Bearer Token
```http
Authorization: Bearer <token>
```

### API Key
```http
X-API-Key: <api-key>
```

## 📝 Manejo de Errores

### Estructura de Error
```json
{
    "success": false,
    "error": {
        "code": "ERROR_CODE",
        "message": "Descripción del error",
        "details": {
            "campo": ["Error específico del campo"]
        }
    }
}
```

### Códigos de Error Comunes

| Código            | Descripción                                    |
|------------------|-----------------------------------------------|
| INVALID_INPUT    | Datos de entrada inválidos                    |
| NOT_FOUND        | Recurso no encontrado                         |
| UNAUTHORIZED     | No autorizado                                 |
| FORBIDDEN        | Acceso prohibido                             |
| SERVER_ERROR     | Error interno del servidor                    |

## 📊 Paginación

### Query Parameters
```http
GET /api/productos?page=1&limit=10
```

### Respuesta Paginada
```json
{
    "success": true,
    "data": [...],
    "pagination": {
        "total": 100,
        "page": 1,
        "pages": 10,
        "limit": 10
    }
}
```

## 🔍 Filtros

### Query Parameters
```http
GET /api/productos?categoria=electronicos&precio_min=100&precio_max=500
```

### Campos Filtrables

| Campo       | Tipo    | Descripción                          |
|------------|---------|-------------------------------------|
| nombre     | string  | Búsqueda por nombre                 |
| categoria  | string  | Filtrar por categoría               |
| precio_min | number  | Precio mínimo                       |
| precio_max | number  | Precio máximo                       |
| stock_min  | number  | Stock mínimo                        |
| stock_max  | number  | Stock máximo                        |

## 📤 Rate Limiting

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1516131012
```

## 🔄 Versioning

```http
Accept: application/vnd.edicommer.v1+json
```

## 📚 SDKs y Clientes

### Python
```python
from edicommer_client import EdiCommerClient

client = EdiCommerClient('api_key')
productos = client.productos.list()
```

### JavaScript
```javascript
const EdiCommer = require('edicommer-js');

const client = new EdiCommer('api_key');
const productos = await client.productos.list();
```

## 🧪 Sandbox

Base URL para pruebas:
```
https://api-sandbox.edicommer.com
```

## 📖 Ejemplos de Uso

### Crear y Actualizar Producto
```python
# Crear producto
producto = {
    "nombre": "Laptop",
    "precio": 999.99,
    "stock": 50
}
response = client.productos.create(producto)

# Actualizar stock
producto_id = response['data']['id']
update = {"stock": 45}
response = client.productos.update(producto_id, update)
```

## 🔐 Seguridad

### CORS
```http
Access-Control-Allow-Origin: *
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Content-Type, Authorization
```

### SSL/TLS
Todo el tráfico debe usar HTTPS