# 🛍️ Sistema de Gestión de Inventario EdiCommer Pro

Sistema avanzado de gestión de inventario y productos desarrollado con arquitectura MVC y patrones de diseño modernos. Permite una gestión completa del ciclo de vida de productos, control de inventario, gestión de ofertas y seguimiento en tiempo real.

## 🏗️ Arquitectura

### Estructura MVC

```
Examen_ArquitecturaSW/
│
├── model/
│   ├── database.py          # Conexión Singleton a SQLite
│   └── producto_model.py    # Acceso a datos de productos
│
├── controller/
│   └── producto_controller.py  # Lógica de negocio y validaciones
│
├── view/
│   └── producto_view.py     # Interfaz de usuario por consola
│
├── main.py                  # Punto de entrada del sistema
└── README.md               # Documentación
```

### Flujo de Datos MVC

1. **Vista (View)**: 
   - Presenta la interfaz al usuario
   - Captura las entradas del usuario
   - Muestra los resultados

2. **Controlador (Controller)**:
   - Recibe las solicitudes de la vista
   - Aplica la lógica de negocio
   - Valida los datos
   - Coordina con el modelo

3. **Modelo (Model)**:
   - Accede a la base de datos
   - Realiza operaciones CRUD
   - Retorna datos al controlador

**Flujo completo**: Usuario → Vista → Controlador → Modelo → Base de Datos → Modelo → Controlador → Vista → Usuario

## 🔧 Patrón Singleton

### Implementación

El patrón Singleton está implementado en `model/database.py` mediante la clase `DatabaseConnection`.

### Características:

- **Garantiza una única instancia**: Aunque se cree múltiples objetos `DatabaseConnection()`, siempre se obtiene la misma instancia.
- **Controla la conexión**: Gestiona una sola conexión a SQLite durante toda la ejecución.
- **Inicialización lazy**: La conexión se crea solo cuando se llama a `connect()`.

### Justificación:

1. **Eficiencia**: Evita múltiples conexiones innecesarias a la base de datos.
2. **Consistencia**: Garantiza que todas las operaciones usen la misma conexión.
3. **Gestión de recursos**: Facilita el cierre y limpieza de la conexión.
4. **Prevención de errores**: Evita problemas de concurrencia en SQLite.

### Ejemplo de uso:

```python
# Ambas variables apuntan a la misma instancia
db1 = DatabaseConnection()
db2 = DatabaseConnection()
# db1 is db2 → True

db1.connect()  # Crea la conexión
conn = db2.get_connection()  # Usa la misma conexión
```

## 📋 Funcionalidades

### Funcionalidades Principales

#### Gestión de Productos
- 📋 **Catálogo Completo**: Vista general con ordenamiento personalizable
- ➕ **Alta de Productos**: Sistema guiado de registro con validaciones
- 📝 **Actualización**: Modificación con seguimiento de cambios
- 🗑️ **Baja de Productos**: Proceso seguro con confirmación
- 🔍 **Consultas Avanzadas**: Búsqueda por múltiples criterios

#### Control de Inventario
- 📊 **Monitoreo de Stock**: Control en tiempo real
- ⚠️ **Alertas Automáticas**: Notificación de stock bajo
- 📦 **Gestión de Reabastecimiento**: Control de niveles mínimos
- 📈 **Historial**: Seguimiento de movimientos

#### Sistema de Ofertas
- 🏷️ **Precios Especiales**: Gestión de ofertas y descuentos
- 📅 **Control Temporal**: Seguimiento de vigencia
- 🎯 **Marcado Automático**: Identificación de productos en oferta

### Sistema de Validaciones

#### Validaciones de Datos
- ✅ **Campos Obligatorios**: 
  - SKU, Nombre, Precio, Categoría
- ✅ **Validaciones Numéricas**:
  - Precios positivos y formato correcto
  - Stock no negativo
  - Stock mínimo válido
- ✅ **Uniqueness**:
  - SKU único en el sistema
  - Control de duplicados

#### Validaciones de Negocio
- ✅ **Precios**:
  - Precio de oferta menor al regular
  - Formato decimal correcto
- ✅ **Stock**:
  - Alertas de nivel bajo
  - Prevención de stock negativo
- ✅ **Estados**:
  - Transiciones válidas de estado
  - Control de productos descontinuados

#### Seguridad
- 🔒 **Sanitización de Entradas**
- 🛡️ **Prevención de SQL Injection**
- 🔍 **Validación de Tipos de Datos**

## 🚀 Instalación y Configuración

### Requisitos del Sistema
- 🐍 Python 3.8 o superior
- 🗃️ MySQL Server 8.0+
- 📦 pip (gestor de paquetes de Python)

### Instalación

1. **Clonar el Repositorio**
```bash
git clone https://github.com/tuusuario/edicommer-pro.git
cd edicommer-pro
```

2. **Instalar Dependencias**
```bash
pip install -r requirements.txt
```

3. **Configurar Base de Datos**
```bash
# Crear base de datos y tablas
mysql -u root -p < init_database.sql
```

4. **Configurar Conexión**
- Editar `model/database.py`
- Ajustar parámetros de conexión:
  ```python
  host = "tu_servidor"
  user = "tu_usuario"
  password = "tu_contraseña"
  database = "edicommer"
  ```

### Ejecución
```bash
python main.py
```

### Verificación
- ✅ Conexión a base de datos exitosa
- ✅ Creación de tablas completada
- ✅ Sistema listo para usar

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

