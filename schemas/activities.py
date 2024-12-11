from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Esquema para crear o actualizar una actividad
class ActivityBase(BaseModel):
    idRelacion: int
    start: datetime
    end: datetime
    title: str
    description: str
    modalityType: str
    color: str
    type: str
    day: int

# Esquema para crear una actividad
class ActivityCreate(ActivityBase):
    scheduleId: str

# Esquema para actualizar una actividad
class ActivityUpdate(ActivityBase):
    id: str = Field(..., alias="_id")

# Esquema para la respuesta de actividad
class ActivityResponse(ActivityBase):
    id: str = Field(..., alias="_id")
    scheduleId: str
