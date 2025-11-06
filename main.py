"""
Archivo principal del sistema de gestión de productos EdiCommer.

Flujo de datos MVC:
1. Vista (View) → Muestra interfaz y recibe entrada del usuario
2. Controlador (Controller) → Procesa la lógica y validaciones
3. Modelo (Model) → Accede a la base de datos
4. Modelo → Controlador → Vista → Usuario (retorno de datos)
"""

from model.database import DatabaseConnection
from controller.producto_controller import ProductoController
from view.producto_view import ProductoView


def main():
    """
    Función principal que inicializa el sistema y maneja el flujo principal.
    """
    # Inicializar conexión a base de datos (Singleton)
    db = DatabaseConnection()
    db.connect()
    
    # Inicializar componentes MVC
    controller = ProductoController()
    view = ProductoView()
    
    print("Bienvenido al Gestor de Productos EdiCommer")
    
    while True:
        view.mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            # Listar productos
            productos = controller.listar_productos()
            view.listar_productos(productos)
            input("\nPresione Enter para continuar...")
        
        elif opcion == "2":
            # Agregar producto
            print("\n--- AGREGAR NUEVO PRODUCTO ---")
            nombre, precio, categoria, stock = view.solicitar_datos_producto()
            exito, mensaje, producto_id = controller.agregar_producto(nombre, precio, categoria, stock)
            
            if exito:
                view.mostrar_mensaje(mensaje, "exito")
            else:
                view.mostrar_mensaje(mensaje, "error")
            
            input("\nPresione Enter para continuar...")
        
        elif opcion == "3":
            # Editar producto
            print("\n--- EDITAR PRODUCTO ---")
            producto_id = view.solicitar_id()
            producto = controller.obtener_producto(producto_id)
            
            if producto:
                view.mostrar_producto(producto)
                print("\nIngrese los nuevos datos (deje en blanco para mantener el valor actual):")
                
                nombre = input(f"Nuevo nombre [{producto['nombre']}]: ").strip() or producto['nombre']
                precio = input(f"Nuevo precio [${producto['precio']}]: ").strip() or producto['precio']
                categoria = input(f"Nueva categoría [{producto['categoria']}]: ").strip() or producto['categoria']
                stock = input(f"Nuevo stock [{producto['stock']}]: ").strip() or producto['stock']
                
                exito, mensaje = controller.editar_producto(producto_id, nombre, precio, categoria, stock)
                
                if exito:
                    view.mostrar_mensaje(mensaje, "exito")
                else:
                    view.mostrar_mensaje(mensaje, "error")
            else:
                view.mostrar_mensaje(f"No existe un producto con ID {producto_id}", "error")
            
            input("\nPresione Enter para continuar...")
        
        elif opcion == "4":
            # Eliminar producto
            print("\n--- ELIMINAR PRODUCTO ---")
            producto_id = view.solicitar_id()
            producto = controller.obtener_producto(producto_id)
            
            if producto:
                view.mostrar_producto(producto)
                confirmar = input("\n¿Está seguro de eliminar este producto? (s/n): ").strip().lower()
                
                if confirmar == 's':
                    exito, mensaje = controller.eliminar_producto(producto_id)
                    if exito:
                        view.mostrar_mensaje(mensaje, "exito")
                    else:
                        view.mostrar_mensaje(mensaje, "error")
                else:
                    view.mostrar_mensaje("Operación cancelada", "info")
            else:
                view.mostrar_mensaje(f"No existe un producto con ID {producto_id}", "error")
            
            input("\nPresione Enter para continuar...")
        
        elif opcion == "5":
            # Consultar producto por ID
            print("\n--- CONSULTAR PRODUCTO ---")
            producto_id = view.solicitar_id()
            producto = controller.obtener_producto(producto_id)
            view.mostrar_producto(producto)
            input("\nPresione Enter para continuar...")
        
        elif opcion == "6":
            # Salir
            print("\n¡Gracias por usar EdiCommer!")
            db.close()
            break
        
        else:
            view.mostrar_mensaje("Opción no válida. Por favor, seleccione una opción del 1 al 6.", "error")
            input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()

