# Modelos de Datos

En este proyecto, los modelos de datos se definen utilizando **Pydantic**. Estos modelos representan las estructuras utilizadas para interactuar con la base de datos y otras partes de la aplicación.

---

## `EventModel`

Este modelo representa un evento. Está definido en `models/event.py`.

### Atributos

| Atributo          | Tipo              | Descripción                                      |
|--------------------|-------------------|--------------------------------------------------|
| `id`              | `Optional[PyObjectId]` | Identificador único del evento (alias: `_id`). |
| `name`            | `str`             | Nombre del evento.                              |
| `description`     | `str`             | Descripción detallada del evento.               |
| `initialHour`     | `str`             | Hora inicial del evento en formato HH:MM.       |
| `initialHourText` | `str`             | Representación textual de la hora inicial.      |
| `finalHour`       | `str`             | Hora final del evento en formato HH:MM.         |
| `finalHourText`   | `str`             | Representación textual de la hora final.        |
| `date`            | `str`             | Fecha del evento en formato ISO 8601.           |
| `isAllDay`        | `bool`            | Indica si el evento dura todo el día.           |
| `reminder`        | `int`             | Tiempo de recordatorio en minutos.              |
| `reminderText`    | `str`             | Representación textual del recordatorio.        |
| `userId`          | `str`             | Identificador único del usuario asociado.       |

### Configuración

- **Tipos arbitrarios permitidos:** Habilitado para usar `PyObjectId`.
- **Codificación JSON:** Convierte instancias de `ObjectId` en cadenas al serializar.

### Ejemplo de Uso

```python
from models.event_model import EventModel

event = EventModel(
    name="Reunión",
    description="Reunión con el equipo",
    initialHour="09:00",
    initialHourText="9:00 AM",
    finalHour="10:00",
    finalHourText="10:00 AM",
    date="2024-12-25",
    isAllDay=False,
    reminder=30,
    reminderText="30 minutos antes",
    userId="user123"
)
print(event.dict(by_alias=True))
```

# `ActivityModel`

El modelo `ActivityModel` representa una actividad que un usuario puede realizar. Está definido en `models/activity_model.py`.

## Atributos

| Atributo          | Tipo              | Descripción                                      |
|--------------------|-------------------|--------------------------------------------------|
| `id`              | `Optional[PyObjectId]` | Identificador único de la actividad (alias: `_id`). |
| `idRelacion`      | `int`             | Identificador relacionado a otra entidad o evento. |
| `start`           | `datetime`        | Fecha y hora de inicio de la actividad.         |
| `end`             | `datetime`        | Fecha y hora de finalización de la actividad.   |
| `title`           | `str`             | Título descriptivo de la actividad.             |
| `description`     | `str`             | Detalles adicionales de la actividad.           |
| `modalityType`    | `str`             | Tipo de modalidad (e.g., "Presencial", "Virtual"). |
| `color`           | `str`             | Color asociado para la representación visual (en formato hexadecimal, e.g., `#FF5733`). |
| `type`            | `str`             | Tipo o categoría de la actividad (e.g., "Clase", "Reunión"). |
| `day`             | `int`             | Día del mes relacionado con la actividad.       |
| `userId`          | `str`             | Identificador único del usuario asociado a la actividad. |

## Configuración

- **Tipos arbitrarios permitidos:** Se permite el uso de `PyObjectId`.
- **Codificación JSON:** Convierte los valores de `ObjectId` a cadenas al serializar el modelo.

## Ejemplo de Uso

```python
from models.activity_model import ActivityModel
from datetime import datetime

# Creación de una instancia de ActivityModel
activity = ActivityModel(
    idRelacion=42,
    start=datetime(2024, 12, 25, 14, 0),
    end=datetime(2024, 12, 25, 16, 0),
    title="Clase de Cálculo Diferencial",
    description="Revisión de temas de derivadas y límites.",
    modalityType="Presencial",
    color="#3A86FF",
    type="Clase",
    day=25,
    userId="user123"
)

# Convertir a diccionario con alias para compatibilidad con MongoDB
print(activity.dict(by_alias=True))
```

## Salida Esperada

Cuando conviertas una instancia de `ActivityModel` a un diccionario o JSON, la salida estará estructurada con los alias definidos. A continuación, se muestra un ejemplo de salida esperada:

```json
{
    "_id": null,
    "idRelacion": 42,
    "start": "2024-12-25T14:00:00",
    "end": "2024-12-25T16:00:00",
    "title": "Clase de Cálculo Diferencial",
    "description": "Revisión de temas de derivadas y límites.",
    "modalityType": "Presencial",
    "color": "#3A86FF",
    "type": "Clase",
    "day": 25,
    "userId": "user123"
}
```


# Nota sobre PyObjectId

El modelo utiliza PyObjectId como tipo para el identificador id, lo que permite trabajar de manera nativa con los ObjectId de MongoDB. Este tipo se serializa automáticamente como una cadena para garantizar la compatibilidad con los formatos JSON.