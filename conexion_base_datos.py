
import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG
from datetime import datetime, timedelta 


def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            pass 
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


def ver_clientes():
    clientes = []
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT cuit, razon_social, correo_contacto FROM clientes")
            clientes = cursor.fetchall()
        except Error as e:
            print(f"Error al obtener clientes: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return clientes

def agregar_cliente(cuit, razon_social, correo_contacto):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO clientes (cuit, razon_social, correo_contacto) VALUES (%s, %s, %s)",
                           (cuit, razon_social, correo_contacto))
            connection.commit()
            return True
        except Error as e:
            print(f"Error al agregar cliente: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False

def modificar_cliente(cuit_original, nuevo_cuit, nueva_razon_social, nuevo_correo_contacto):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE clientes SET cuit = %s, razon_social = %s, correo_contacto = %s WHERE cuit = %s",
                           (nuevo_cuit, nueva_razon_social, nuevo_correo_contacto, cuit_original))
            connection.commit()
            return True
        except Error as e:
            print(f"Error al modificar cliente: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False

def eliminar_cliente(cuit):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM clientes WHERE cuit = %s", (cuit,))
            connection.commit()
            return True
        except Error as e:
            print(f"Error al eliminar cliente: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False



def ver_destinos():
    destinos = []
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, pais, ciudad, costo_base FROM destinos")
            destinos = cursor.fetchall()
        except Error as e:
            print(f"Error al obtener destinos: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return destinos

def agregar_destino(pais, ciudad, costo_base):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO destinos (pais, ciudad, costo_base) VALUES (%s, %s, %s)",
                           (pais, ciudad, costo_base))
            connection.commit()
            return True
        except Error as e:
            print(f"Error al agregar destino: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False

def modificar_destino(destino_id, nuevo_pais, nueva_ciudad, nuevo_costo_base):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE destinos SET pais = %s, ciudad = %s, costo_base = %s WHERE id = %s",
                           (nuevo_pais, nueva_ciudad, nuevo_costo_base, destino_id))
            connection.commit()
            return True
        except Error as e:
            print(f"Error al modificar destino: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False

def eliminar_destino(destino_id):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM destinos WHERE id = %s", (destino_id,))
            connection.commit()
            return True
        except Error as e:
            print(f"Error al eliminar destino: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False



def ver_ventas():
    ventas = []
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            query = """
            SELECT v.id, v.fecha_venta, v.costo, v.estado, v.fecha_anulacion,
                   c.cuit, c.razon_social AS cliente_razon_social,
                   d.pais AS destino_pais, d.ciudad AS destino_ciudad, d.costo_base AS destino_costo_base
            FROM ventas v
            JOIN clientes c ON v.cuit_cliente = c.cuit
            JOIN destinos d ON v.destino_id = d.id
            ORDER BY v.fecha_venta DESC
            """
            cursor.execute(query)
            ventas = cursor.fetchall()
        except Error as e:
            print(f"Error al obtener ventas: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return ventas

def registrar_venta(cuit_cliente, destino_id, costo):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            fecha_venta = datetime.now()
            cursor.execute("INSERT INTO ventas (cuit_cliente, destino_id, fecha_venta, costo, estado) VALUES (%s, %s, %s, %s, %s)",
                           (cuit_cliente, destino_id, fecha_venta, costo, 'ACTIVA'))
            connection.commit()
            return True
        except Error as e:
            print(f"Error al registrar venta: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False

def anular_venta(venta_id):
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT fecha_venta, estado FROM ventas WHERE id = %s", (venta_id,))
            venta = cursor.fetchone()

            if venta:
                if venta['estado'] == 'Anulada':
                    print("La venta ya ha sido anulada.")
                    return False

                fecha_venta = venta['fecha_venta']
                tiempo_limite = fecha_venta + timedelta(minutes=5)
                
                if datetime.now() <= tiempo_limite:
                    cursor.execute("UPDATE ventas SET estado = 'Anulada', fecha_anulacion = %s WHERE id = %s",
                                   (datetime.now(), venta_id))
                    connection.commit()
                    return True
                else:
                    print(f"No se pudo anular la venta. El tiempo límite es de 5 minutos ")
                    return False
            else:
                print("Venta no encontrada.")
                return False
        except Error as e:
            print(f"Error al anular venta: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False
