
from datetime import datetime, timedelta
from conexion_base_datos import ver_clientes as db_ver_clientes, \
                                ver_destinos as db_ver_destinos, \
                                ver_ventas as db_ver_ventas, \
                                registrar_venta as db_registrar_venta, \
                                anular_venta as db_anular_venta


def gestionar_ventas():
    while True:
        print("\n-- GESTIONAR VENTAS --")
        print("1. Ver Ventas")
        print("2. Registrar Venta")
        print("3. Volver al Menú Principal")

        opcion_venta = input("Seleccione una opción: ")

        if opcion_venta == "1":
            print(">> Eligió opción 1: Ver Ventas")
            ver_ventas()
        elif opcion_venta == "2":
            print(">> Eligió opción 2: Registrar Venta")
            registrar_venta()
        elif opcion_venta == "3":
            print(">> Salió de 'Gestionar Ventas'")
            break
        else:
            print("Opción no válida.")

def registrar_venta():
    print("\n--- REGISTRAR VENTA ---")

    clientes_disponibles = db_ver_clientes()
    if not clientes_disponibles:
        print("No hay clientes registrados.")
        return

    print("\n--- CLIENTES DISPONIBLES ---")
    for cliente in clientes_disponibles:
        print(f"CUIT: {cliente['cuit']}, Razón Social: {cliente['razon_social']}")
    cuit_cliente = input("Ingrese el CUIT del cliente: ")

    cliente_encontrado = None
    for c in clientes_disponibles:
        if c['cuit'] == cuit_cliente:
            cliente_encontrado = c
            break

    if not cliente_encontrado:
        print("Cliente no encontrado.")
        return

    destinos_disponibles = db_ver_destinos()
    if not destinos_disponibles:
        print("No hay destinos registrados.")
        return

    print("\n--- DESTINOS DISPONIBLES ---")
    for destino in destinos_disponibles:
        print(f"ID: {destino['id']}, País: {destino['pais']}, Ciudad: {destino['ciudad']}, Costo Base: {destino['costo_base']:.2f}")

    try:
        id_destino = int(input("Ingrese el ID del destino: "))
    except ValueError:
        print("ID de destino inválido.")
        return

    destino_encontrado = None
    for d in destinos_disponibles:
        if d['id'] == id_destino:
            destino_encontrado = d
            break

    if not destino_encontrado:
        print("Destino no encontrado.")
        return

    costo_venta = destino_encontrado['costo_base']

    if db_registrar_venta(cuit_cliente, id_destino, costo_venta):
        print("Venta registrada con éxito.")
    else:
        print("Error al registrar la venta.")

def ver_ventas():
    print("\n--- LISTA DE VENTAS REGISTRADAS ---")
    ventas_db = db_ver_ventas()
    if not ventas_db:
        print("No hay ventas registradas.")
    else:
        for venta in ventas_db:
            fecha_venta_str = venta['fecha_venta'].strftime("%Y-%m-%d %H:%M:%S") if isinstance(venta['fecha_venta'], datetime) else "N/A"
            fecha_anulacion_str = venta['fecha_anulacion'].strftime("%Y-%m-%d %H:%M:%S") if isinstance(venta['fecha_anulacion'], datetime) else "N/A"
            print(f"ID Venta: {venta['id']}, Fecha: {fecha_venta_str}, Cliente: {venta['cuit']}, "
                  f"Destino ID: {venta['id']}, Costo: {venta['costo']:.2f}, " 
                  f"Estado: {venta['estado']}")

def boton_arrepentimiento():
    while True:
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        print("1. Anular Venta Reciente")
        print("2. Ver Ventas Anuladas")
        print("3. Volver al Menú Principal")

        opcion_arrepentimiento = input("Seleccione una opción: ")

        if opcion_arrepentimiento == "1":
            print(">> Eligió opción 1: Anular Venta Reciente")
            anular_venta()
        elif opcion_arrepentimiento == "2":
            print(">> Eligió opción 2: Ver Ventas Anuladas")
            ver_ventas_anuladas()
        elif opcion_arrepentimiento == "3":
            print(">> Salió de 'Botón de Arrepentimiento'")
            break
        else:
            print("Opción no válida.")

def anular_venta():
    print("\n--- ANULAR VENTA RECIENTE ---\n")
    try:
        venta_id = int(input("Ingrese el ID de la venta que desea anular: "))
        ahora = datetime.now()
    except ValueError:
        print("ID de venta inválido.")
        return

    if db_anular_venta(venta_id):
        print("Venta anulada con éxito.")
   

def ver_ventas_anuladas():
    print("\n--- LISTA DE VENTAS ANULADAS ---")
    ventas = db_ver_ventas()
    anuladas = [venta for venta in ventas if venta.get("estado") == "Anulada"]

    if not anuladas:
        print("No hay ventas anuladas registradas.")
    else:
        for venta in anuladas:
            fecha_venta_str = venta['fecha_venta'].strftime("%Y-%m-%d %H:%M:%S") if isinstance(venta['fecha_venta'], datetime) else "N/A"
            fecha_anulacion_str = venta['fecha_anulacion'].strftime("%Y-%m-%d %H:%M:%S") if isinstance(venta['fecha_anulacion'], datetime) else "N/A"
            print(f"ID Venta: {venta['id']}, Fecha Venta: {fecha_venta_str}, Cliente: {venta['cuit']}, "
                  f"Destino ID: {venta['id']}, Costo: {venta['costo']:.2f}, " 
                  f"Fecha Anulación: {fecha_anulacion_str}")