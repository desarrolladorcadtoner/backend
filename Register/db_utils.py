# db_utils.py
import pyodbc
from .config import DATABASE_CONFIG1
from .config import DATABASE_DistProd

def get_db_connection():
    conn_str = (
        f"DRIVER={DATABASE_CONFIG1['DRIVER']};"
        f"SERVER={DATABASE_CONFIG1['SERVER']};"
        f"DATABASE={DATABASE_CONFIG1['DATABASE']};"
        f"UID={DATABASE_CONFIG1['UID']};"
        f"PWD={DATABASE_CONFIG1['PWD']}"
    )
    return pyodbc.connect(conn_str)

def get_prod_connection():
    conn_prod = (
        f"DRIVER={DATABASE_DistProd['DRIVER']};"
        f"SERVER={DATABASE_DistProd['SERVER']};"
        f"DATABASE={DATABASE_DistProd['DATABASE']};"
        f"UID={DATABASE_DistProd['UID']};"
        f"PWD={DATABASE_DistProd['PWD']}"
    )
    return pyodbc.connect(conn_prod)


def fetch_regimen_sat(tipo_persona: str):
    # Seleccionar la columna a filtrar según el tipo de persona
    column_filter = "RegimenSATPF" if tipo_persona == "fisica" else "RegimenSATPM"
    query = f"""
        SELECT RegimenSATId, RegimenSATDescripcion
        FROM [AuroFiscal].[dbo].[RegimenSAT]
        WHERE {column_filter} = 1
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        regimenes = [
            {
                "RegimenSATId": row.RegimenSATId,
                "RegimenSATDescripcion": row.RegimenSATDescripcion
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return regimenes
    except Exception as e:
        return {"error": str(e)}


def fetch_productos():
    query = "SELECT * FROM Productos$"
    try:
        conn = get_prod_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        productos = [
            {
                "id": row.id,
                "nombre": row.nombre,
                "precio": row.precio,
                "stock": row.stock,
                "imagen": row.imagen
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return productos
    except Exception as e:
        return {"error": str(e)}

def insert_producto(nombre: str, precio: float, stock: int, imagen: str):
    query = """
        INSERT INTO Productos$ (nombre, precio, stock, imagen)
        VALUES (?,  ?, ?, ?)
    """
    try:
        conn = get_prod_connection()
        cursor = conn.cursor()
        cursor.execute(query, (nombre, precio, stock, imagen))
        conn.commit()
        conn.close()
        return {"mensaje": "Producto creado con éxito"}
    except Exception as e:
        return {"error": str(e)}
