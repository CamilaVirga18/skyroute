
from gestion_clientes import gestionar_clientes
from gestion_destinos import gestionar_destinos
from gestion_ventas import gestionar_ventas, boton_arrepentimiento
from conexion_base_datos import get_db_connection 

def mostrar_menu():
    print("\nBienvenidos a SkyRoute - Sistema de Gestión de Pasajes")
    print("1. Gestionar Clientes")
    print("2. Gestionar Destinos")
    print("3. Gestionar Ventas")
    print("4. Botón de Arrepentimiento")
    print("5. Salir del Sistema")


if __name__ == "__main__":
    print("Intentando conectar a la base de datos...")
    conn = get_db_connection()
    if conn:
        print("Conexión inicial a la base de datos establecida.")
        conn.close()
    else:
        print("No se pudo establecer una conexión inicial a la base de datos. Verifique la configuración y el servidor MySQL.")
        

    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print(">> Eligió 'Gestionar Clientes'")
            gestionar_clientes()
        elif opcion == "2":
            print(">> Eligió 'Gestionar Destinos'")
            gestionar_destinos()
        elif opcion == "3":
            print(">> Eligió 'Gestionar Ventas'")
            gestionar_ventas()
        elif opcion == "4":
            print(">> Eligió 'Botón de Arrepentimiento'")
            boton_arrepentimiento()
        elif opcion == "5":
            print("\n>> Eligió 'Salir del Sistema'.")
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")