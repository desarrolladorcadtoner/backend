# Register/endpoints.py
from fastapi import APIRouter, HTTPException, Query
from Register.db_utils import fetch_regimen_sat, fetch_usos_cfdi_descripcion

router = APIRouter()

@router.get("/regi-sat")
def get_regimen_sat(tipo_persona: str = Query(..., pattern="^(fisica|moral)$")):
    try:
        regimenes = fetch_regimen_sat(tipo_persona)
        if isinstance(regimenes, dict) and "error" in regimenes:
            raise Exception(regimenes["error"])
        return {"regimen_sat": regimenes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/usos-cfdi-descripcion/{regimen_sat_id}")
def get_usos_cfdi_descripcion(regimen_sat_id: int):
    try:
        resultados = fetch_usos_cfdi_descripcion(regimen_sat_id)
        if isinstance(resultados, dict) and "error" in resultados:
            raise HTTPException(status_code=500, detail=resultados["error"])
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
