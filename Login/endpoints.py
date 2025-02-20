from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .db_utils import validar_usuario

router = APIRouter()

class LoginRequest(BaseModel):
    usuario: str
    password: str

class LoginResponse(BaseModel):
    message: str

@router.post("/login", response_model=LoginResponse)
async def login(request: LoginRequest):
    if validar_usuario(request.usuario, request.password):
        return {"message": "Usuario válido"}
    else:
        raise HTTPException(status_code=401, detail="Usuario inválido")
