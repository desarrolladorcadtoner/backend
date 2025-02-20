# Register/db_utils.py
import pyodbc
from Server.config import DATABASE_AuroFiscal

def get_AFiscal_connection():
    conn_str = (
        f"DRIVER={DATABASE_AuroFiscal['DRIVER']};"
        f"SERVER={DATABASE_AuroFiscal['SERVER']};"
        f"DATABASE={DATABASE_AuroFiscal['DATABASE']};"
        f"UID={DATABASE_AuroFiscal['UID']};"
        f"PWD={DATABASE_AuroFiscal['PWD']}"
    )
    return pyodbc.connect(conn_str)

def fetch_regimen_sat(tipo_persona: str):
    # Seleccionar la columna según el tipo de persona
    column_filter = "RegimenSATPF" if tipo_persona == "fisica" else "RegimenSATPM"
    query = f"""
        SELECT RegimenSATId, RegimenSATDescripcion
        FROM [AuroFiscal].[dbo].[RegimenSAT]
        WHERE {column_filter} = 1
    """
    try:
        conn = get_AFiscal_connection()
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

def fetch_usos_cfdi_descripcion(regimen_sat_id: int):
    query = """
        SELECT C.c_UsosCFDI, C.DescripcionUsoCFDI
        FROM [AuroFiscal].[dbo].[UsosCFDIRegimenes] U
        JOIN [AuroFiscal].[dbo].[UsosCFDI] C ON U.c_UsosCFDI = C.c_UsosCFDI
        WHERE U.RegimenSATId = ?
    """
    try:
        conn = get_AFiscal_connection()  
        cursor = conn.cursor()
        cursor.execute(query, (regimen_sat_id,))
        resultados = [
            {
                "c_UsosCFDI": row.c_UsosCFDI,
                "DescripcionUsoCFDI": row.DescripcionUsoCFDI
            }
            for row in cursor.fetchall()
        ]
        conn.close()
        return resultados
    except Exception as e:
        return {"error": str(e)}
