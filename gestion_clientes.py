clientes = {}

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
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cuit, cliente in clientes.items():
            print(f"CUIT: {cuit}, Razón Social: {cliente['razon_social']}, Correo: {cliente['correo_contacto']}")

def agregar_cliente():
    print("\n--- AGREGAR CLIENTE ---")
    razon_social = input("Ingrese la razon social: ")
    cuit = input("Ingrese el CUIT : ")
    correo_contacto = input("Ingrese el correo: ")

    if cuit not in clientes:
        clientes[cuit] = {
            "razon_social": razon_social,
            "correo_contacto": correo_contacto
        }
        print("Cliente agregado con éxito.")
    else:
        print("Ya existe un cliente con ese CUIT.")

def modificar_cliente():
    print("\n--- MODIFICAR CLIENTE (incluye cambio de CUIT) ---")
    cuit = input("Ingrese el CUIT del cliente a modificar: ")
    if cuit in clientes:
        nuevo_cuit = input("Ingrese el nuevo CUIT: ")
        nuevo_razon = input("Ingrese la nueva razon social: ")
        nuevo_correo_contacto = input("Ingrese el nuevo Correo de Contacto: ")

        clientes[nuevo_cuit] = {
            "razon_social": nuevo_razon,
            "correo_contacto": nuevo_correo_contacto
        }
        if nuevo_cuit != cuit:
            del clientes[cuit]
        print("Cliente modificado con éxito.")
    else:
        print("No existe un cliente con ese CUIT.")

def eliminar_cliente():
    print("\n--- ELIMINAR CLIENTE ---")
    cuit = input("Ingrese el CUIT del cliente a eliminar: ")
    if cuit in clientes:
        del clientes[cuit]
        print("Cliente eliminado con éxito.")
    else:
        print("No existe un cliente con ese CUIT.")
