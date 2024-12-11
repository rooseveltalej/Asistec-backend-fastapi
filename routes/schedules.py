from fastapi import APIRouter
from schemas.activities import ActivityCreate, ActivityUpdate
from controllers.schedules import (
    create_activity,
    get_user_activities,
    update_activity,
    delete_activity,
    delete_activities_by_relation_id
)

router = APIRouter()

@router.post("/registerActivity/{user_id}")
async def register_activity(user_id: str, activity_data: ActivityCreate):
    return await create_activity(user_id, activity_data.dict())


@router.get("/getActivities/{user_id}")
async def get_activities(user_id: str):
    return await get_user_activities(user_id)

@router.put("/updateActivity/{activity_id}")
@router.put("/updateActivity/{activity_id}")
async def update_activity_route(activity_id: str, activity_data: ActivityUpdate):
    return await update_activity(activity_id, activity_data.dict())

@router.delete("/deleteActivity/{activity_id}")
async def delete_activity_route(activity_id: str):
    return await delete_activity(activity_id)

@router.delete("/deleteActivitiesByRelationId/{relation_id}")
async def delete_activities_by_relation_id_route(relation_id: int):
    return await delete_activities_by_relation_id(relation_id)
