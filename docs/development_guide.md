# Guía de Desarrollo - EdiCommer Pro

## 🚀 Inicio Rápido para Desarrolladores

### Preparación del Entorno

1. **Configurar Entorno de Desarrollo**
```bash
# Clonar repositorio
git clone https://github.com/tuusuario/edicommer-pro.git
cd edicommer-pro

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows

# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt
```

2. **Configurar Pre-commit Hooks**
```bash
pre-commit install
```

## 📝 Guías de Estilo

### Estilo de Código Python

Seguimos [PEP 8](https://www.python.org/dev/peps/pep-0008/) con algunas modificaciones:

```python
# ✅ Correcto
class ProductoController:
    def agregar_producto(self, nombre: str, precio: float) -> tuple:
        """
        Agrega un nuevo producto.
        
        Args:
            nombre: Nombre del producto
            precio: Precio del producto
            
        Returns:
            tuple: (éxito, mensaje, id)
        """
        return True, "Éxito", 1

# ❌ Incorrecto
class productoController:
    def AgregarProducto(self,nombre,precio):
        return True,"Éxito",1
```

### Convenciones de Nombres

- 🔷 **Clases**: PascalCase
- 🔶 **Funciones**: snake_case
- 🔸 **Variables**: snake_case
- 🔺 **Constantes**: UPPER_CASE

## 🏗️ Arquitectura

### Estructura de Carpetas

```
edicommer-pro/
├── model/              # Capa de datos
├── view/              # Interfaces de usuario
├── controller/        # Lógica de negocio
├── docs/             # Documentación
```

### Flujo de Trabajo Git

1. **Branches**
```bash
# Crear nueva feature
git checkout -b feature/nueva-funcionalidad

# Crear fix
git checkout -b fix/bug-description
```

2. **Commits**
```bash
# Formato de commit
feat: añadir búsqueda por categoría
fix: corregir validación de precio
docs: actualizar README
```

## 🧪 Testing

### Escribir Tests

```python
import unittest
from model.producto_model import ProductoModel

class TestProductoModel(unittest.TestCase):
    def setUp(self):
        self.model = ProductoModel()
    
    def test_crear_producto(self):
        resultado = self.model.crear("Test", 100)
        self.assertTrue(resultado[0])
```

### Ejecutar Tests

```bash
# Ejecutar todos los tests
python -m unittest discover

# Ejecutar test específico
python -m unittest tests.test_producto
```

## 🔄 CI/CD

### GitHub Actions

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Tests
        run: python -m unittest discover
```

## 🐛 Debugging

### VSCode Launch Configuration

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```

### Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debugging información")
logger.info("Información general")
logger.warning("Advertencia")
logger.error("Error")
```

## 📦 Gestión de Dependencias

### Añadir Nuevas Dependencias

```bash
# Instalar y agregar a requirements.txt
pip install package-name
pip freeze > requirements.txt
```

### Actualizar Dependencias

```bash
pip install --upgrade -r requirements.txt
```

## 🔒 Seguridad

### Buenas Prácticas

1. **Manejo de Secretos**
```python
# ✅ Correcto
from decouple import config
DB_PASSWORD = config('DB_PASSWORD')

# ❌ Incorrecto
DB_PASSWORD = "password123"
```

2. **Validación de Entrada**
```python
# ✅ Correcto
def procesar_entrada(datos):
    if not isinstance(datos, dict):
        raise ValueError("Datos inválidos")
    
# ❌ Incorrecto
def procesar_entrada(datos):
    # Procesar sin validar
```

## 📝 Documentación

### Docstrings

```python
def validar_producto(producto: dict) -> tuple[bool, str]:
    """
    Valida los datos de un producto.

    Args:
        producto (dict): Datos del producto a validar
            {
                'nombre': str,
                'precio': float,
                'stock': int
            }

    Returns:
        tuple[bool, str]: (éxito, mensaje)

    Raises:
        ValueError: Si los datos son inválidos
    """
    pass
```

### Comentarios

```python
# TODO: Implementar validación adicional
# FIXME: Corregir problema de concurrencia
# NOTE: Esta función asume que el producto existe
```

## 🤝 Contribuir

### Proceso de Pull Request

1. Fork del repositorio
2. Crear branch descriptiva
3. Implementar cambios
4. Escribir/actualizar tests
5. Crear Pull Request

### Checklist de PR

- [ ] Tests pasan
- [ ] Linting pasa
- [ ] Documentación actualizada
- [ ] Cambios probados localmente

## 📚 Recursos

### Herramientas Recomendadas

- 📝 VS Code con extensiones:
  - Python
  - GitLens
  - Python Test Explorer
- 🐛 PyCharm (alternativa)

### Enlaces Útiles

- 📘 [Documentación de Python](https://docs.python.org/)
- 📗 [MySQL Documentation](https://dev.mysql.com/doc/)
- 📙 [Git Book](https://git-scm.com/book/)