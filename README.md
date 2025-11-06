# 🛍️ Sistema de Gestión de Inventario EdiCommer Pro

Sistema de gestión de inventario desarrollado con arquitectura MVC y MySQL. Implementa operaciones CRUD básicas para la gestión de productos con una interfaz de consola intuitiva y fácil de usar.

## ✨ Características Principales

- 📝 **Gestión Completa de Productos**
  - Crear nuevos productos
  - Listar inventario existente
  - Actualizar información
  - Eliminar productos
  - Consultar por ID

- 🏗️ **Arquitectura MVC Limpia**
  - Separación clara de responsabilidades
  - Código organizado y mantenible
  - Patrón Singleton para conexión a BD

- 🔒 **Base de Datos MySQL**
  - Conexión segura a Clever Cloud
  - Persistencia de datos
  - Consultas optimizadas

## 🏗️ Arquitectura del Sistema

### Estructura del Proyecto

```
Examen_ArquitecturaSW/
│
├── model/
│   ├── database.py          # Conexión Singleton a MySQL
│   └── producto_model.py    # Modelo de datos de productos
│
├── controller/
│   └── producto_controller.py  # Lógica de negocio
│
├── view/
│   └── producto_view.py     # Interfaz de consola
│
├── docs/                    # Documentación detallada
│   ├── technical_guide.md
│   ├── installation_guide.md
│   ├── development_guide.md
│   ├── api_reference.md
│   └── database.md
│
├── images/                  # Capturas de pantalla
│   ├── agregar nuevo producto.png
│   ├── Consultar por ID.png
│   ├── Editar producto.png
│   ├── Eliminar Producto.png
│   └── listar productos.png
│
├── main.py                 # Punto de entrada
└── README.md              # Documentación general
```

### Componentes MVC

1. **Modelo (Model)**:
   - `database.py`: Implementa el patrón Singleton para la conexión a MySQL
   - `producto_model.py`: Define la estructura y operaciones de datos

2. **Vista (View)**:
   - `producto_view.py`: Interfaz de consola interactiva
   - Manejo de entrada/salida del usuario
   - Presentación de datos formateada

3. **Controlador (Controller)**:
   - `producto_controller.py`: Coordina el flujo de datos
   - Implementa la lógica de negocio
   - Gestiona las operaciones CRUD

## 🔧 Patrón Singleton para Conexión a Base de Datos

La clase `DatabaseConnection` en `model/database.py` implementa el patrón Singleton para gestionar la conexión a MySQL de manera eficiente:

```python
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### Ventajas:

- ✨ **Conexión Única**: Una sola instancia para toda la aplicación
- 🔄 **Reutilización**: La misma conexión se comparte entre componentes
- 📊 **Eficiencia**: Evita múltiples conexiones innecesarias
- 🛡️ **Consistencia**: Garantiza integridad en las operaciones de BD

## 📋 Operaciones CRUD

### Gestión de Productos

#### 1. Crear Producto ➕
- Nombre del producto
- Descripción detallada
- Precio
- Stock inicial
- ![Crear Producto](images/agregar%20nuevo%20producto.png)

#### 2. Listar Productos 📋
- Vista de todo el inventario
- Formato de tabla clara
- Todos los detalles del producto
- ![Listar Productos](images/listar%20productos.png)

#### 3. Consultar por ID 🔍
- Búsqueda rápida por ID
- Detalles completos del producto
- ![Consultar Producto](images/Consultar%20por%20ID.png)

#### 4. Actualizar Producto 📝
- Modificación de cualquier campo
- Validación de datos
- Actualización inmediata
- ![Editar Producto](images/Editar%20producto.png)

#### 5. Eliminar Producto 🗑️
- Eliminación segura
- Confirmación requerida
- ![Eliminar Producto](images/Eliminar%20Producto.png)

### Validaciones

- ✅ Campos requeridos completos
- 🔢 Valores numéricos válidos
- 📝 Datos con formato correcto
- 🛡️ Protección contra SQL injection

## 🚀 Instalación

### Requisitos
- 🐍 Python 3.8+
- 📦 mysql-connector-python

### Pasos de Instalación

1. **Clonar el Repositorio**
```bash
git clone https://github.com/GABRIEL-708/ExamenArquitecturaSW.git
cd ExamenArquitecturaSW
```

2. **Instalar Dependencias**
```bash
pip install mysql-connector-python
```

3. **Configurar Base de Datos**
- La conexión está preconfigurada a una base de datos MySQL en Clever Cloud
- No se requiere configuración adicional

### Ejecución
```bash
python main.py
```

## 📚 Documentación

Para información más detallada, consulta:

- 📖 [Guía Técnica](docs/technical_guide.md)
- 🛠️ [Guía de Instalación](docs/installation_guide.md)
- 👨‍💻 [Guía de Desarrollo](docs/development_guide.md)
- 🔄 [Referencia de API](docs/api_reference.md)
- 🗃️ [Documentación de Base de Datos](docs/database.md)

## 📝 Gestión Avanzada de Productos

### Campos del Producto
- 🔑 **ID**: Identificador único auto-incrementado
- 📦 **SKU**: Código único de producto (requerido)
- 📝 **Nombre**: Nombre del producto (requerido)
- 📄 **Descripción**: Detalles completos del producto
- 💰 **Precio Regular**: Precio base del producto (requerido)
- 🏷️ **Precio Oferta**: Precio promocional (opcional)
- 🏷️ **Categoría**: Categoría principal del producto (requerido)
- 🏷️ **Subcategoría**: Clasificación secundaria (opcional)
- ™️ **Marca**: Marca del producto (opcional)
- 📦 **Stock Actual**: Cantidad disponible en inventario
- ⚠️ **Stock Mínimo**: Nivel de alerta para reabastecimiento
- 📏 **Unidad de Medida**: Unidad de venta del producto
- 📅 **Fecha Creación**: Registro automático de creación
- 🔄 **Última Actualización**: Seguimiento de modificaciones
- 🚦 **Estado**: Control de estado del producto (activo/descontinuado/en_oferta)

### Características Avanzadas
- 🔍 Búsqueda y filtrado avanzado
- 📊 Seguimiento de inventario en tiempo real
- 🏷️ Sistema integrado de ofertas
- ⚠️ Alertas de stock bajo
- 📈 Historial de actualizaciones
- 🔒 Validaciones robustas de datos

## 🎯 Características del Sistema

- Arquitectura MVC clara y separada
- Patrón Singleton para gestión de conexión
- Interfaz de consola intuitiva
- Validaciones robustas
- Base de datos SQLite persistente
- Código documentado y comentado

## �️ Stack Tecnológico

### Tecnologías Core
- 🐍 **Python 3.8+**: Lenguaje principal de desarrollo
- 🗃️ **MySQL**: Sistema de gestión de base de datos
- 🏗️ **Arquitectura MVC**: Patrón de diseño estructural
- 🔒 **Singleton Pattern**: Gestión eficiente de conexiones

### Librerías y Dependencias
- 🔌 **mysql-connector-python**: Conexión y gestión de MySQL
- 🎨 **colorama**: Interfaz de consola mejorada
- 📊 **tabulate**: Formateo profesional de tablas

### Características Técnicas
- 🔐 **Prepared Statements**: Prevención de SQL Injection
- 🔄 **Conexiones Pooling**: Gestión eficiente de recursos
- 🔍 **Índices Optimizados**: Búsquedas de alta velocidad
- 🌐 **UTF-8**: Soporte completo de caracteres internacionales

### Herramientas de Desarrollo
- 🐙 **Git**: Control de versiones
- 📝 **VS Code**: Entorno de desarrollo
- 🐛 **Debugging Tools**: Herramientas de depuración avanzada

## 👨‍💻 Autor

Sistema desarrollado para el examen de Arquitectura de Software.

