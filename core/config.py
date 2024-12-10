from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"  #Archivo de variables de entorno

settings = Settings()
