# Configuración del Proyecto

Este proyecto utiliza Pydantic Settings para manejar la configuración mediante un archivo de variables de entorno (.env). Esto permite definir configuraciones clave como la conexión a la base de datos de manera segura y flexible.

---

## Configuración de Variables de Entorno

La clase Settings está definida en core/config.py y es responsable de cargar las variables de entorno.

### Descripción de la Configuración

- BaseSettings: Clase base proporcionada por Pydantic para gestionar configuraciones basadas en variables de entorno.
- MONGO_URI: URI de conexión a la base de datos MongoDB.
- DATABASE_NAME: Nombre de la base de datos a utilizar.
- Config.env_file: Define el nombre del archivo de entorno desde el cual se cargarán las variables.

---

## Archivo .env

Crea un archivo .env en la raíz del proyecto con las siguientes variables:

MONGO_URI=mongodb://localhost:27017  
DATABASE_NAME=mi_base_de_datos

### Detalles de las Variables

- MONGO_URI: Proporciona la URI de conexión para la base de datos MongoDB. Puede incluir credenciales, host, puerto y opciones específicas, como mongodb://user:password@host:port/dbname.
- DATABASE_NAME: Nombre de la base de datos a la que se conectará el proyecto.

### Ejemplo de Uso
El objeto settings se puede utilizar directamente en el código para acceder a las configuraciones:

```python
from core.config import settings

print(settings.MONGO_URI)        # Salida: mongodb://localhost:27017
print(settings.DATABASE_NAME)    # Salida: mi_base_de_datos
```

---

## Beneficios de Usar BaseSettings

1. Separación de Configuración del Código:  
   Mantener las configuraciones en un archivo externo mejora la seguridad y la organización.

2. Compatibilidad con Entornos Diferentes:  
   Cambia las configuraciones fácilmente entre entornos de desarrollo, pruebas y producción.

3. Validación Automática:  
   Pydantic valida automáticamente los tipos de datos de las variables de entorno.

---

Con esta configuración, puedes gestionar de manera eficiente las variables sensibles y específicas de cada entorno. Para añadir nuevas configuraciones, simplemente actualiza la clase Settings y el archivo .env.
