from pydantic import BaseModel, Field
from typing import Dict, List, Union

# Esquema para el contenido individual del evento
class EventContent(BaseModel):
    date: str
    description: str
    finalHour: str
    finalHourText: str
    id: str
    initialHour: str
    initialHourText: str
    isAllDay: bool
    name: str
    reminder: int
    reminderText: str

# Esquema para la creación de eventos
class EventCreate(BaseModel):
    eventItems: Dict[str, List[EventContent]] = Field(
        ..., description="Mapa de fechas y listas de eventos para cada fecha"
    )

# Esquema para la actualización de eventos
class EventUpdate(BaseModel):
    eventItems: Dict[str, List[EventContent]] = Field(
        ..., description="Mapa de fechas y listas de eventos para actualizar"
    )

# Esquema para la respuesta de un evento
class EventResponse(EventCreate):
    id: str = Field(..., alias="_id")
