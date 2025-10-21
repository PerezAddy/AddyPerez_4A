# Controlador encargado de la lógica de autenticación
# Nos sirve para separar la lógica del login y mantener limpia la interfaz

from database import crear_conexion
from mysql.connector import Error

def validar_credenciales(usuario, password):
    """
    Valida las credenciales del usuario en la base de datos.
    Retorna True si el usuario y contraseña coinciden, False en caso contrario.
    """
    conexion = crear_conexion()  # ✅ Llamada correcta a la función (no es método)
    
    if not conexion:
        return False
    cursor = None
    try:
        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        cursor.execute(consulta, (usuario, password))
        resultado = cursor.fetchone()
        return bool(resultado)
    except Error as e:
        print(f"Error en la validación de credenciales: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexion.is_connected():
            conexion.close()