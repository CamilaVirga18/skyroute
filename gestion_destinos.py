
from conexion_base_datos import ver_destinos as db_ver_destinos, \
                                agregar_destino as db_agregar_destino, \
                                modificar_destino as db_modificar_destino, \
                                eliminar_destino as db_eliminar_destino

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
    destinos_db = db_ver_destinos() 
    if not destinos_db:
        print("No hay destinos registrados.")
    else:
        for destino in destinos_db:
            print(f"ID: {destino['id']}, País: {destino['pais']}, Ciudad: {destino['ciudad']}, Costo Base: {destino['costo_base']:.2f}")

def agregar_destino():
    print("\n--- AGREGAR DESTINO ---")
    pais = input("Ingrese el País: ")
    ciudad = input("Ingrese la Ciudad: ")
    try:
        costo_base = float(input("Ingrese el Costo Base: "))
    except ValueError:
        print("Costo base inválido. Por favor, ingrese un número.")
        return
    
    if db_agregar_destino(pais, ciudad, costo_base): 
        print("Destino agregado con éxito.")
    else:
        print("Error al agregar destino.")

def modificar_destino():
    print("\n--- MODIFICAR DESTINO ---")
    try:
        destino_id = int(input("Ingrese el ID del destino a modificar: "))
    except ValueError:
        print("ID de destino inválido. Por favor, ingrese un número.")
        return

    
    destinos_existentes = db_ver_destinos()
    destino_encontrado = False
    for d in destinos_existentes:
        if d['id'] == destino_id:
            destino_encontrado = True
            break

    if destino_encontrado:
        nuevo_pais = input("Ingrese el nuevo País: ")
        nueva_ciudad = input("Ingrese la nueva Ciudad: ")
        try:
            nuevo_costo_base = float(input("Ingrese el nuevo Costo Base: "))
        except ValueError:
            print("Costo base inválido. Por favor, ingrese un número.")
            return

        if db_modificar_destino(destino_id, nuevo_pais, nueva_ciudad, nuevo_costo_base): 
            print("Destino modificado con éxito.")
        else:
            print("Error al modificar destino.")
    else:
        print("No existe un destino con ese ID.")

def eliminar_destino():
    print("\n--- ELIMINAR DESTINO ---")
    try:
        destino_id = int(input("Ingrese el ID del destino a eliminar: "))
    except ValueError:
        print("ID de destino inválido. Por favor, ingrese un número.")
        return
    
   
    destinos_existentes = db_ver_destinos()
    if not any(d['id'] == destino_id for d in destinos_existentes):
        print("No existe un destino con ese ID.")
        return

    if db_eliminar_destino(destino_id): 
        print("Destino eliminado con éxito.")
    else:
        print("Error al eliminar destino.")