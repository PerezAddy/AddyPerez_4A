from database import crear_conexion
from mysql.connector import Error 

def ver_pedido():
    """Obtiene todos los pedidos de la base de datos."""
    conexion = crear_conexion()
    if not conexion:
        return []
    
    cursor = None
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            SELECT id_pedido, nombre_cliente, fecha_entrega, descripcion, precio_total, abono
            FROM pedidos
        """)
        resultado = cursor.fetchall()
        return resultado
        
    except Error as e:
        print(f"Error al obtener pedidos: {e}")
        return []
        
    finally:
        if cursor:
            cursor.close()
        if conexion and conexion.is_connected():
            conexion.close()


def crear_pedido(nombre_cliente, fecha_entrega, descripcion, precio_total, abono):
    """Crea un nuevo pedido en la base de datos."""
    conexion = crear_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            INSERT INTO pedidos (nombre_cliente, fecha_entrega, descripcion, precio_total, abono)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre_cliente, fecha_entrega, descripcion, precio_total, abono))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al crear pedido: {e}")
        return False
    finally:
        if conexion and conexion.is_connected():
            conexion.close()


def actualizar_pedido(id_pedido, nombre_cliente, fecha_entrega, descripcion, precio_total, abono):
    """Actualiza un pedido existente por su ID."""
    conexion = crear_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        cursor.execute("""
            UPDATE pedidos 
            SET nombre_cliente = %s, fecha_entrega = %s, descripcion = %s, precio_total = %s, abono = %s
            WHERE id_pedido = %s
        """, (nombre_cliente, fecha_entrega, descripcion, precio_total, abono, id_pedido))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar pedido: {e}")
        return False
    finally:
        if conexion and conexion.is_connected():
            conexion.close()


def eliminar_pedido(id_pedido):
    """Elimina un pedido por su ID."""
    conexion = crear_conexion()
    if not conexion:
        return False
    
    try:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM pedidos WHERE id_pedido = %s", (id_pedido,))
        conexion.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar pedido: {e}")
        return False
    finally:
        if conexion and conexion.is_connected():
            conexion.close()
