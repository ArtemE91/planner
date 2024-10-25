from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException, status

from database.objects import Database
from models.events import Event, EventUpdate

event_router = APIRouter(tags=["Event"])
event_database = Database(Event)


@event_router.get("/", response_model=list[Event])
async def retrieve_all_events() -> list[Event]:
    events = await event_database.get_all()
    return events


@event_router.get("/{event_id}", response_model=Event)
async def retrieve_event(event_id: PydanticObjectId) -> Event:
    event = await event_database.get(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return event


@event_router.post("/")
async def create_event(body: Event) -> dict:
    await event_database.create(body)
    return {"message": "Event created successfully"}


@event_router.put("/{event_id}", response_model=Event)
async def update_event(event_id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(event_id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return updated_event


@event_router.delete("/{event_id}")
async def delete_event(event_id: PydanticObjectId) -> dict:
    event = await event_database.delete(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event with supplied ID does not exist"
        )
    return {"message": "Event deleted successfully."}