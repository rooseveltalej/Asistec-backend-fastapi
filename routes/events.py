from fastapi import APIRouter
from schemas.events import EventCreate, EventUpdate
from controllers.events import create_event, get_user_events, update_event, delete_event

router = APIRouter()

@router.post("/registerEvent/{user_id}")
async def register_event(user_id: str, event_data: EventCreate):
    return await create_event(user_id, event_data.dict())

@router.get("/getEvents/{user_id}")
async def get_events(user_id: str):
    return await get_user_events(user_id)

@router.put("/updateEvent/{event_id}")
async def update_event_route(event_id: str, event_data: EventUpdate):
    return await update_event(event_id, event_data.dict())

@router.delete("/deleteEvent/{event_id}")
async def delete_event_route(event_id: str):
    return await delete_event(event_id)
