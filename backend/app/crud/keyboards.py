from typing import List, Union
from app.schemas.keyboards import KeyboardPayloadSchema
from app.models.keyboard import Keyboard
from app.models.seller_site import SellerSite
from app.models.description import Description
from sqlalchemy.orm import Session


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

    description_id = payload.description_id
    description = db.query(Description).filter(Description.id == description_id).first()

    if description:
        keyboard.description = description
        db.commit()
        db.refresh(keyboard)

    return keyboard.id


async def get_one(id: int, db: Session) -> Union[dict, None]:
    query = db.query(Keyboard).filter(Keyboard.id == id).first()

    if query:
        return query
    return None


async def get_all(db: Session) -> List:
    query = db.query(Keyboard).all()
    return query
