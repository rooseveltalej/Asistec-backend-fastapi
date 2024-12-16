from fastapi import HTTPException
from bson import ObjectId
from db.mongo_client import mongo_client
from models.event import EventModel

db = mongo_client.get_database()

async def create_event(user_id: str, event_data: dict):
    # Validar si el usuario existe
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    event_data["userId"] = user_id
    try:
        result = await db["events"].insert_one(event_data)
        return {"message": "Evento creado correctamente", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear el evento: {str(e)}")

async def get_user_events(user_id: str):
    # Validar si el usuario existe
    user = await db["users"].find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    events = await db["events"].find({"userId": user_id}).to_list(100)
    return [{"_id": str(event["_id"]), **event} for event in events]

async def update_event(event_id: str, event_data: dict):
    try:
        updated_event = await db["events"].find_one_and_update(
            {"_id": ObjectId(event_id)},
            {"$set": event_data},
            return_document=True
        )
        if not updated_event:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        return {"message": "Evento actualizado correctamente", "event": updated_event}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el evento: {str(e)}")

async def delete_event(event_id: str):
    try:
        result = await db["events"].delete_one({"_id": ObjectId(event_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Evento no encontrado")
        return {"message": "Evento eliminado correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el evento: {str(e)}")
