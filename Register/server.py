# server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .db_utils import fetch_regimen_sat, fetch_productos, insert_producto
from fastapi import FastAPI, HTTPException, Query

from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get("/regi-sat")
def get_regimen_sat(tipo_persona: str = Query(..., pattern="^(fisica|moral)$")):
    try:
        regimenes = fetch_regimen_sat(tipo_persona)
        if isinstance(regimenes, dict) and "error" in regimenes:
            raise Exception(regimenes["error"])
        return {"regimen_sat": regimenes}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/productos")
def get_productos():
    try:
        productos = fetch_productos()
        if isinstance(productos, dict) and "error" in productos:
            raise Exception(productos["error"])
        return productos  # Se devuelve la lista directamente
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ProductoSchema(BaseModel):
    nombre: str
    precio: float
    stock: int
    imagen: str

@app.post("/productos/agregarProducto")
def add_producto(producto: ProductoSchema):
    try:
        resultado = insert_producto(producto.nombre, producto.precio, producto.stock, producto.imagen)
        if isinstance(resultado, dict) and "error" in resultado:
            raise Exception(resultado["error"])
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))