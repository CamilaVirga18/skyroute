from datetime import datetime, timedelta
from gestion_clientes import clientes, ver_clientes
from gestion_destinos import destinos, ver_destinos

ventas = []

def generar_venta_id():
    return len(ventas) + 1

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
    ver_clientes()
    cuit_cliente = input("Ingrese el CUIT del cliente que realiza la compra: ")
    if cuit_cliente not in clientes:
        print("No existe un cliente con ese CUIT.")
        return

    ver_destinos()
    destino_id = int(input("Ingrese el ID del destino del viaje: "))
    if destino_id not in destinos:
        print("No existe un destino con ese ID.")
        return

    fecha_venta = datetime.now()
    costo = float(input("Ingrese el costo del viaje: "))

    venta_id = generar_venta_id()
    venta = {
        "venta_id": venta_id,
        "cuit_cliente": cuit_cliente,
        "destino_id": destino_id,
        "fecha_venta": fecha_venta,
        "costo": costo,
        "estado": "Activa"
    }
    ventas.append(venta)
    print("Venta registrada con éxito.")

def ver_ventas():
    print("\n--- LISTA DE VENTAS ---")
    if not ventas:
        print("No hay ventas registradas.")
    else:
        for venta in ventas:
            fecha = venta["fecha_venta"].strftime("%Y-%m-%d")
            print(f"Venta ID: {venta['venta_id']}, Cliente: {venta['cuit_cliente']}, Destino ID: {venta['destino_id']}, Fecha: {fecha}, Costo: {venta['costo']}, Estado: {venta['estado']}")

def boton_arrepentimiento():
    while True:
        print("\n-- BOTÓN DE ARREPENTIMIENTO --")
        print("1. Ver Ventas Anuladas")
        print("2. Anular Venta Reciente")
        print("3. Volver al Menú Principal")

        opcion_arrepentimiento = input("Seleccione una opción: ")

        if opcion_arrepentimiento == "1":
            print(">> Eligió opción 1: Ver Ventas Anuladas")
            ver_ventas_anuladas()
        elif opcion_arrepentimiento == "2":
            print(">> Eligió opción 2: Anular Venta Reciente")
            anular_venta()
        elif opcion_arrepentimiento == "3":
            print(">> Salió de 'Boton de Arrepentimiento'")
            break
        else:
            print("Opción no válida.")

def anular_venta():
    print("\n--- ANULAR VENTA RECIENTE ---")
    venta_id = int(input("Ingrese el ID de la venta que desea anular: "))
    ahora = datetime.now()

    for venta in ventas:
        if venta["venta_id"] == venta_id:
            if venta["estado"] == "Anulada":
                print("La venta ya fue anulada.")
                return
            tiempo_venta = venta["fecha_venta"]
            if ahora - tiempo_venta <= timedelta(minutes=5):
                venta["estado"] = "Anulada"
                venta["fecha_anulacion"] = ahora
                print("Venta anulada con éxito.")
            else:
                print("La venta no puede anularse porque pasaron más de 10 minutos.")
            return
    print("No se encontró ninguna venta con ese ID.")

def ver_ventas_anuladas():
    print("\n--- LISTA DE VENTAS ANULADAS ---")
    anuladas = [venta for venta in ventas if venta["estado"] == "Anulada"]

    if not anuladas:
        print("No hay ventas anuladas registradas.")
    else:
        for venta in anuladas:
            fecha = venta.get("fecha_anulacion", "Fecha no disponible")
            if isinstance(fecha, datetime):
                fecha = fecha.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Venta ID: {venta['venta_id']}, Cliente: {venta['cuit_cliente']}, Destino ID: {venta['destino_id']}, Fecha de Anulación: {fecha}")
