from fastapi import HTTPException
from models.activity import ActivityModel
from db.mongo_client import mongo_client
from bson import ObjectId


db = mongo_client.get_database()

# Crear una nueva actividad
async def create_activity(user_id: str, activity_data: dict):
    user = await db["users"].find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=400, detail="El usuario no existe")

    activity_data["userId"] = user_id
    try:
        result = await db["activities"].insert_one(activity_data)
        return {"message": "Actividad creada correctamente", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear la actividad: {str(e)}")

# Obtener actividades de un usuario
async def get_user_activities(user_id: str):
    # Validar y convertir user_id a ObjectId
    try:
        user_object_id = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="ID de usuario inválido")

    # Verificar si el usuario existe
    user = await db["users"].find_one({"_id": user_object_id})
    if not user:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    # Obtener el schedule asociado al user_id
    schedule = await db["schedules"].find_one({"userId": str(user_object_id)})
    if not schedule:
        raise HTTPException(status_code=404, detail="No se encontró un horario para este usuario")

    # Usar scheduleId para buscar las actividades
    activities = await db["activities"].find({"scheduleId": str(schedule["_id"])}).to_list(100)

    # Serializar el campo _id de las actividades
    serialized_activities = [
        {**activity, "_id": str(activity["_id"])} for activity in activities
    ]

    return {"activities": serialized_activities}

# Actualizar una actividad
async def update_activity(activity_id: str, activity_data: dict):
    try:
        updated_activity = await db["activities"].find_one_and_update(
            {"_id": ObjectId(activity_id)},
            {"$set": activity_data},
            return_document=True
        )
        if not updated_activity:
            raise HTTPException(status_code=404, detail="Actividad no encontrada")
        return {"message": "Actividad actualizada correctamente", "activity": updated_activity}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la actividad: {str(e)}")

# Eliminar una actividad
async def delete_activity(activity_id: str):
    try:
        result = await db["activities"].delete_one({"_id": ObjectId(activity_id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Actividad no encontrada")
        return {"message": "Actividad eliminada correctamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la actividad: {str(e)}")

# Eliminar actividades relacionadas por idRelacion
async def delete_activities_by_relation_id(relation_id: int):
    try:
        result = await db["activities"].delete_many({"idRelacion": relation_id})
        return {"message": f"Actividades eliminadas: {result.deleted_count}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar actividades relacionadas: {str(e)}")
