from typing import List
from fastapi import APIRouter, HTTPException
from app.crud.keyboards import post, get_one, get_all
from app.schemas.keyboards import (
    KeyboardPayloadSchema,
    KeyboardResponseSchema,
    KeyboardSchema,
)

from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=KeyboardResponseSchema, status_code=201)
async def create_keyboard(
    payload: KeyboardPayloadSchema, db: Session = Depends(get_db)
) -> KeyboardResponseSchema:
    kb_id = await post(payload, db)

    response_object = {
        "id": kb_id,
        "name": payload.name,
        "url": payload.url,
        "price": payload.price,
        "seller_site_id": payload.seller_site_id,
        "image": payload.image,
        "description": payload.description,
    }

    return response_object


@router.get("/{id}/", response_model=KeyboardSchema)
async def read_one_keyboard(id: int, db: Session = Depends(get_db)) -> KeyboardSchema:
    seller_site = await get_one(id, db)

    return seller_site


@router.get("/", response_model=List[KeyboardSchema])
async def read_all_keyboards(db: Session = Depends(get_db)) -> List[KeyboardSchema]:
    return await get_all(db)
