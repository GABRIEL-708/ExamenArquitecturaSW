# Guía de Instalación de EdiCommer Pro

## 📋 Requisitos Previos

### Software Necesario
- 🐍 Python 3.8 o superior
- 🗃️ MySQL Server 8.0+
- 📦 pip (gestor de paquetes de Python)
- 🐙 Git (opcional, para clonar el repositorio)

### Requisitos del Sistema
- 💻 Sistema Operativo: Windows/Linux/MacOS
- 🔧 2GB RAM mínimo
- 💾 500MB espacio en disco

## 🚀 Proceso de Instalación

### 1. Preparación del Entorno

#### Windows
```powershell
# Verificar versión de Python
python --version

# Verificar pip
pip --version
```

#### Linux/MacOS
```bash
# Verificar versión de Python
python3 --version

# Verificar pip
pip3 --version
```

### 2. Obtener el Código

#### Usando Git
```bash
# Clonar repositorio
git clone https://github.com/tuusuario/edicommer-pro.git
cd edicommer-pro
```

#### Descarga Manual
1. Descargar ZIP del repositorio
2. Extraer en la ubicación deseada
3. Abrir terminal en la carpeta extraída

### 3. Configuración del Entorno Virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
## Windows
venv\Scripts\activate
## Linux/MacOS
source venv/bin/activate
```

### 4. Instalar Dependencias

```bash
# Instalar requerimientos
pip install -r requirements.txt
```

### 5. Configuración de Base de Datos

#### Crear Base de Datos
```sql
-- Ejecutar en MySQL
CREATE DATABASE edicommer;
```

#### Inicializar Esquema
```bash
# Ejecutar script de inicialización
mysql -u root -p edicommer < init_database.sql
```

#### Configurar Conexión
Editar `model/database.py`:
```python
# Configuración de conexión
config = {
    "host": "localhost",
    "user": "tu_usuario",
    "password": "tu_contraseña",
    "database": "edicommer"
}
```

## 🔧 Verificación de la Instalación

### 1. Probar Conexión
```python
# Ejecutar Python
from model.database import DatabaseConnection

db = DatabaseConnection()
conn = db.connect()
# Debería conectarse sin errores
```

### 2. Ejecutar Tests
```bash
# Ejecutar suite de pruebas
python -m unittest discover tests
```

### 3. Iniciar Aplicación
```bash
# Ejecutar programa principal
python main.py
```

## 🔍 Solución de Problemas

### Problemas Comunes

#### Error de Conexión MySQL
```
Error: No se puede conectar a MySQL
```
**Solución:**
1. Verificar que MySQL está ejecutándose
2. Comprobar credenciales
3. Verificar firewall

#### Error de Dependencias
```
ModuleNotFoundError: No module named 'mysql'
```
**Solución:**
```bash
pip install mysql-connector-python
```

#### Error de Permisos
```
Access denied for user
```
**Solución:**
```sql
GRANT ALL PRIVILEGES ON edicommer.* TO 'usuario'@'localhost';
FLUSH PRIVILEGES;
```

## 📝 Notas Adicionales

### Actualizaciones
- Revisar regularmente el repositorio
- Actualizar dependencias:
  ```bash
  pip install --upgrade -r requirements.txt
  ```

### Respaldo
- Respaldar base de datos:
  ```bash
  mysqldump -u root -p edicommer > backup.sql
  ```

### Seguridad
- Cambiar contraseñas por defecto
- Mantener MySQL actualizado
- Revisar permisos de archivos

## 🆘 Soporte

### Canales de Ayuda
- 📧 Correo: soporte@edicommer.com
- 💬 Discord: [Enlace]
- 📝 Issues de GitHub

### Recursos Adicionales
- 📚 [Documentación de MySQL](https://dev.mysql.com/doc/)
- 🐍 [Python MySQL Connector](https://dev.mysql.com/doc/connector-python/en/)
- 📖 [Wiki del Proyecto](https://github.com/tuusuario/edicommer-pro/wiki)