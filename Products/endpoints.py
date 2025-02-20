# Products/endpoints.py
from fastapi import APIRouter, HTTPException
from .db_utils import fetch_productos, insert_producto, fetch_producto_by_id
from pydantic import BaseModel

router = APIRouter()

@router.get("/productos")
def get_productos():
    try:
        productos = fetch_productos()
        if isinstance(productos, dict) and "error" in productos:
            raise Exception(productos["error"])
        return productos
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ProductoSchema(BaseModel):
    nombre: str
    precio: float
    stock: int
    imagen: str

@router.post("/productos/agregarProducto")
def add_producto(producto: ProductoSchema):
    try:
        resultado = insert_producto(producto.nombre, producto.precio, producto.stock, producto.imagen)
        if isinstance(resultado, dict) and "error" in resultado:
            raise Exception(resultado["error"])
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/productos/{producto_id}")
def get_producto(producto_id: int):
    try:
        producto = fetch_producto_by_id(producto_id)
        if isinstance(producto, dict) and "error" in producto:
            raise HTTPException(status_code=404, detail=producto["error"])
        return producto
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
