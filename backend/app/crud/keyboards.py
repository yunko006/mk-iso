from typing import List, Union
from app.schemas.keyboards import KeyboardPayloadSchema
from app.models.keyboard import Keyboard
from app.models.seller_site import SellerSite
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends


async def post(payload: KeyboardPayloadSchema, db: Session) -> int:
    keyboard = Keyboard(
        name=payload.name, url=payload.url, price=payload.price, image=payload.image
    )

    db.add(keyboard)
    db.commit()
    db.refresh(keyboard)

    seller_site_id = payload.seller_site_id
    seller_site = db.query(SellerSite).filter(SellerSite.id == seller_site_id).first()

    if seller_site:
        keyboard.seller_site = seller_site
        db.commit()
        db.refresh(keyboard)
    return keyboard.id


async def get_one(id: int, db: Session) -> Union[dict, None]:
    query = db.query(Keyboard).filter(Keyboard.id == id).first()

    if query:
        return query
    return None


async def get_all(db: Session) -> List:
    seller_sites = db.query(Keyboard).all()
    return seller_sites
