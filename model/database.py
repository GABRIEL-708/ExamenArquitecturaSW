"""
Módulo de conexión a base de datos usando el patrón Singleton.

Patrón Singleton:
- Asegura que solo exista una instancia de la conexión a la base de datos
- Evita múltiples conexiones innecesarias y mejora el rendimiento
- Centraliza la gestión de la conexión en un solo punto
"""

import mysql.connector
from mysql.connector import Error


class DatabaseConnection:
    """
    Clase Singleton para la conexión a la base de datos MySQL.
    
    Justificación del patrón Singleton:
    - Garantiza una única conexión a la base de datos durante toda la ejecución
    - Evita problemas de concurrencia y múltiples conexiones abiertas
    - Facilita el mantenimiento y la gestión de recursos
    """
    
    _instance = None
    _connection = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance
    
    def connect(self, host='localhost', user='root', password='', database='edicommer'):
        """
        Conecta a la base de datos MySQL.
        
        Args:
            host (str): Host de la base de datos
            user (str): Usuario de MySQL
            password (str): Contraseña de MySQL
            database (str): Nombre de la base de datos
        """
        if self._connection is None:
            try:
                print("Intentando conectar a la base de datos en Clever Cloud...")
                config = {
                    "host": "bsgru36cv5yhisoln20d-mysql.services.clever-cloud.com",
                    "user": "urj89clk903d2hgj",
                    "password": "lrqYml6k7m015umYldH",
                    "database": "bsgru36cv5yhisoln20d",
                    "connect_timeout": 30,
                    "port": 21957,
                    "ssl_disabled": True,
                    "use_pure": True,
                    "auth_plugin": 'mysql_native_password'
                }
                print(f"Conectando a: {config['host']}")
                print(f"Base de datos: {config['database']}")
                self._connection = mysql.connector.connect(**config)
                print("¡Conexión exitosa!")
                self._create_tables()
            except Error as e:
                print(f"Error detallado: {str(e)}")
                if e.errno == 2003:
                    print("No se puede alcanzar el servidor. Verifica tu conexión a internet y que el servidor esté disponible.")
                elif e.errno == 1045:
                    print("Error de autenticación. Verifica usuario y contraseña.")
                elif e.errno == 1049:
                    print("La base de datos no existe.")
                raise Exception(f"Error al conectar a MySQL: {e}")
        
        return self._connection
    
    def _create_tables(self):
        """Crea las tablas necesarias si no existen."""
        cursor = self._connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(255) NOT NULL,
                precio DECIMAL(10,2) NOT NULL,
                categoria VARCHAR(100) NOT NULL,
                stock INT NOT NULL DEFAULT 0,
                fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                ultima_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
        ''')
        self._connection.commit()
    
    def get_connection(self):
        """
        Obtiene la conexión actual.
        
        Returns:
            mysql.connector.connection.MySQLConnection: Conexión a la base de datos
        
        Raises:
            Exception: Si la conexión no ha sido inicializada
        """
        if self._connection is None:
            raise Exception("La conexión no ha sido inicializada. Llama a connect() primero.")
        return self._connection
    
    def close(self):
        """Cierra la conexión a la base de datos."""
        if self._connection:
            self._connection.close()
            self._connection = None

