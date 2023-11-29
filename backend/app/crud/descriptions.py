from typing import List, Union
from app.schemas.descriptions import DescriptionPayloadSchema
from app.models.keyboard import Keyboard
from app.models.description import Description
from sqlalchemy.orm import Session


# api is not posting any descriptions atm
"""
async def post(payload: DescriptionPayloadSchema, db: Session) -> int:
    description = Description(
        layout=payload.layout,
        brand=payload.brand,
        product_type=payload.product_type,
        profile=payload.profile,
        layout_size=payload.layout_size,
        layout_standard=payload.layout_standard,
        layout_ergonomics=payload.layout_ergonomics,
        hot_swappable=payload.hot_swappable,
        knob_support=payload.knob_support,
        rgb_support=payload.rgb_support,
        display_support=payload.display_support,
        qmk_via_support=payload.qmk_via_support,
        connection=payload.connection,
        battery_capacity=payload.battery_capacity,
        mount_style=payload.mount_style,
        case_material=payload.case_material,
        keycap_material=payload.keycap_material,
        # keyboard id ?
    )

    db.add(description)
    db.commit()
    db.refresh(description)

    kb_id = payload.keyboard_id
    kb = db.query(Keyboard).filter(Keyboard.id == kb_id).first()

    if kb:
        description.keyboards = kb
        db.commit()
        db.refresh(description)
"""


async def get_one(id: int, db: Session) -> Union[dict, None]:
    query = db.query(Description).filter(Description.id == id).first()

    if query:
        return query
    return None


async def get_all(db: Session) -> List:
    query = db.query(Description).all()
    return query
