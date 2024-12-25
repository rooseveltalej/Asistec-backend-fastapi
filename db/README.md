# Configuración de la Base de Datos

Este proyecto utiliza **MongoDB** como base de datos, conectándose a través del cliente asíncrono `motor`. Toda la configuración relacionada a la base de datos se encuentra en el archivo `db/mongo_client.py`.

## Estructura del Archivo

El archivo `db/mongo_client.py` incluye:
- Una clase `MongoClient` que maneja la conexión a la base de datos.
- Un objeto global `mongo_client` para acceder a la base de datos desde cualquier parte del proyecto.

## Dependencias Requeridas

Antes de usar la configuración de la base de datos, asegúrate de instalar las dependencias necesarias:

```bash
pip install motor
```

Configuración

La conexión a la base de datos depende de dos variables configuradas en el archivo de configuración global (core/config):
	•	MONGO_URI: La URI de conexión a MongoDB. Incluye credenciales y la dirección del servidor.
	•	DATABASE_NAME: El nombre de la base de datos que utilizará el proyecto.

Para realizar operaciones con la base de datos, importa y utiliza el objeto mongo_client desde cualquier parte del proyecto.

# Ejemplo

```python
from db.mongo_client import mongo_client

async def example_function():
    # Obtén la base de datos
    db = mongo_client.get_database()
    
    # Define la colección
    collection = db["nombre_de_la_coleccion"]
    
    # Realiza una consulta
    result = await collection.find_one({"clave": "valor"})
    print(result)
```

En este ejemplo:
	1.	Obtenemos una instancia de la base de datos con mongo_client.get_database().
	2.	Definimos la colección que queremos usar.
	3.	Ejecutamos una consulta con la sintaxis asíncrona de Motor.