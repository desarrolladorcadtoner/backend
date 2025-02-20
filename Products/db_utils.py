# Products/db_utils.py
import pyodbc
from Server.config import DATABASE_DistProd

def get_prod_connection():
    conn_str = (
        f"DRIVER={DATABASE_DistProd['DRIVER']};"
        f"SERVER={DATABASE_DistProd['SERVER']};"
        f"DATABASE={DATABASE_DistProd['DATABASE']};"
        f"UID={DATABASE_DistProd['UID']};"
        f"PWD={DATABASE_DistProd['PWD']}"
    )
    return pyodbc.connect(conn_str)

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
        VALUES (?, ?, ?, ?)
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

def fetch_producto_by_id(producto_id: int):
    query = """
        SELECT id, nombre, precio, stock, referencia, categoria, linprod, imagen
        FROM [DistBD].[dbo].[Productos$]
        WHERE id = ?
    """
    try:
        conn = get_prod_connection()
        cursor = conn.cursor()
        cursor.execute(query, (producto_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return {
                "id": row.id,
                "nombre": row.nombre,
                "precio": row.precio,
                "stock": row.stock,
                "referencia": row.referencia,
                "categoria": row.categoria,
                "linprod": row.linprod,
                "imagen": row.imagen
            }
        else:
            return {"error": "Producto no encontrado"}
    except Exception as e:
        return {"error": str(e)}
