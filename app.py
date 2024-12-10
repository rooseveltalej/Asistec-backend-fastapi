from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.users import router as users_router
from db.mongo_client import mongo_client

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes (es inseguro en producción)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    print("Aplicación iniciada. MongoDB conectado.")

@app.on_event("shutdown")
async def shutdown_event():
    mongo_client.client.close()
    print("Aplicación cerrada. Conexión a MongoDB cerrada.")

# Registrar rutas
app.include_router(users_router, prefix="/usuarios", tags=["Usuarios"])

@app.get("/")
async def root():
    return {"message": "API FUNCIONANDO"}