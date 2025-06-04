
from conexion_base_datos import ver_clientes as db_ver_clientes, \
                                agregar_cliente as db_agregar_cliente, \
                                modificar_cliente as db_modificar_cliente, \
                                eliminar_cliente as db_eliminar_cliente

def gestionar_clientes():
    while True:
        print("\n-- GESTIONAR CLIENTES --")
        print("1. Ver Clientes")
        print("2. Agregar Cliente")
        print("3. Modificar Cliente")
        print("4. Eliminar Cliente")
        print("5. Volver al Menú Principal")

        opcion_cliente = input("\nSeleccione una opción: ")

        if opcion_cliente == "1":
            print(">> Eligió opción 1: Ver Clientes")
            ver_clientes()
        elif opcion_cliente == "2":
            print(">> Eligió opción 2: Agregar Cliente")
            agregar_cliente()
        elif opcion_cliente == "3":
            print(">> Eligió opción 3: Modificar Cliente")
            modificar_cliente()
        elif opcion_cliente == "4":
            print(">> Eligió opción 4: Eliminar Cliente")
            eliminar_cliente()
        elif opcion_cliente == "5":
            print(">> Salió de 'Gestionar Clientes'")
            break
        else:
            print("Opción no válida.")

def ver_clientes():
    print("\n--- LISTA DE CLIENTES ---")
    clientes_db = db_ver_clientes() #
    if not clientes_db:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes_db:
            print(f"CUIT: {cliente['cuit']}, Razón Social: {cliente['razon_social']}, Correo: {cliente['correo_contacto']}")

def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")
    cuit = input("Ingrese el CUIT del cliente: ")

  
    clientes_existentes = db_ver_clientes()
    if any(c['cuit'] == cuit for c in clientes_existentes):
        print("Error: Ya existe un cliente con ese CUIT.")
        return

    razon_social = input("Ingrese la Razón Social: ")
    correo_contacto = input("Ingrese el Correo de Contacto: ")
    
    if db_agregar_cliente(cuit, razon_social, correo_contacto): 
        print("Cliente agregado con éxito.")
    else:
        print("Error al agregar cliente.")

def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE (incluye cambio de CUIT) ---")
    cuit = input("Ingrese el CUIT del cliente a modificar: ")
    
    
    clientes_existentes = db_ver_clientes()
    cliente_encontrado = None
    for c in clientes_existentes:
        if c['cuit'] == cuit:
            cliente_encontrado = c
            break

    if cliente_encontrado:
        nuevo_cuit = input(f"Ingrese el nuevo CUIT (actual: {cliente_encontrado['cuit']}): ")
        nuevo_razon = input(f"Ingrese la nueva razon social (actual: {cliente_encontrado['razon_social']}): ")
        nuevo_correo_contacto = input(f"Ingrese el nuevo Correo de Contacto (actual: {cliente_encontrado['correo_contacto']}): ")
        
        
        if db_modificar_cliente(cuit, nuevo_cuit, nuevo_razon, nuevo_correo_contacto):
            print("Cliente modificado con éxito.")
        else:
            print("Error al modificar cliente.")
    else:
        print("No existe un cliente con ese CUIT.")

def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")
    cuit = input("Ingrese el CUIT del cliente a eliminar: ")
    
    
    clientes_existentes = db_ver_clientes()
    if not any(c['cuit'] == cuit for c in clientes_existentes):
        print("No existe un cliente con ese CUIT.")
        return

    if db_eliminar_cliente(cuit): 
        print("Cliente eliminado con éxito.")
    else:
        print("Error al eliminar cliente.")