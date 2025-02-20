import pyodbc
from Server.config import DATABASE_DistProd

def get_db_connection():
    conn_str = (
        f"DRIVER={DATABASE_DistProd['DRIVER']};"
        f"SERVER={DATABASE_DistProd['SERVER']};"
        f"DATABASE={DATABASE_DistProd['DATABASE']};"
        f"UID={DATABASE_DistProd['UID']};"
        f"PWD={DATABASE_DistProd['PWD']}"
    )
    return pyodbc.connect(conn_str)

def validar_usuario(usuario: str, password: str) -> bool:
    """
    Consulta la tabla [Usuarios] para validar las credenciales.
    Se asume que los campos son [Usuario] y [Password].
    """
    query = """
        SELECT COUNT(*) FROM [DistBD].[dbo].[Usuarios]
        WHERE Usuario = ? AND Password = ?
    """
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute(query, (usuario, password))
    resultado = cursor.fetchone()[0]
    cursor.close()
    conexion.close()
    return resultado > 0