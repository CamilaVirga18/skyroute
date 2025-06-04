destinos = {}

def generar_destino_id():
    return len(destinos) + 1

def gestionar_destinos():
    while True:
        print("\n-- GESTIONAR DESTINOS --")
        print("1. Ver Destinos")
        print("2. Agregar Destino")
        print("3. Modificar Destino")
        print("4. Eliminar Destino")
        print("5. Volver al Menú Principal")

        opcion_destino = input("\nSeleccione una opción: ")

        if opcion_destino == "1":
            print(">> Eligió opción 1: Ver Destinos")
            ver_destinos()
        elif opcion_destino == "2":
            print(">> Eligió opción 2: Agregar Destino")
            agregar_destino()
        elif opcion_destino == "3":
            print(">> Eligió opción 3: Modificar Destino")
            modificar_destino()
        elif opcion_destino == "4":
            print(">> Eligió opción 4: Eliminar Destino")
            eliminar_destino()
        elif opcion_destino == "5":
            print(">> Salió de 'Gestionar Destinos'")
            break
        else:
            print("Opción no válida.")

def ver_destinos():
    print("\n--- LISTA DE DESTINOS ---")
    if not destinos:
        print("No hay destinos registrados.")
    else:
        for destino_id, destino in destinos.items():
            print(f"Destino ID: {destino_id}, País: {destino['pais']}, Ciudad: {destino['ciudad']}, Costo Base: {destino['costo_base']}")

def agregar_destino():
    print("\n--- AGREGAR DESTINO ---")
    pais = input("Ingrese el País del destino: ")
    ciudad = input("Ingrese la Ciudad del destino: ")
    costo_base = float(input("Ingrese el Costo Base del viaje: "))

    destino_id = generar_destino_id()
    destinos[destino_id] = {
        "pais": pais,
        "ciudad": ciudad,
        "costo_base": costo_base
    }
    print("Destino agregado con éxito.")

def modificar_destino():
    print("\n--- MODIFICAR DESTINO ---")
    destino_id = int(input("Ingrese el ID del destino a modificar: "))
    if destino_id in destinos:
        nuevo_pais = input("Ingrese el nuevo País: ")
        nueva_ciudad = input("Ingrese la nueva Ciudad: ")
        nuevo_costo_base = float(input("Ingrese el nuevo Costo Base: "))
        destinos[destino_id] = {
            "pais": nuevo_pais,
            "ciudad": nueva_ciudad,
            "costo_base": nuevo_costo_base
        }
        print("Destino modificado con éxito.")
    else:
        print("No existe un destino con ese ID.")

def eliminar_destino():
    print("\n--- ELIMINAR DESTINO ---")
    destino_id = int(input("Ingrese el ID del destino a eliminar: "))
    if destino_id in destinos:
        del destinos[destino_id]
        print("Destino eliminado con éxito.")
    else:
        print("No existe un destino con ese ID.")
