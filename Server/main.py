# Server/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importamos los routers de cada módulo (las rutas se definen en cada carpeta)
from Register.endpoints import router as register_router
from Products.endpoints import router as products_router
from Login.endpoints import router as login_router

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montamos los routers con un prefijo y etiquetas
app.include_router(register_router, prefix="/register", tags=["Registro"])
app.include_router(products_router, prefix="/productos", tags=["Productos"])
app.include_router(login_router, prefix="/login", tags=["Login"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("Server.main:app", host="0.0.0.0", port=8000, reload=True)
