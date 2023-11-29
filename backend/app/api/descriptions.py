from typing import List
from fastapi import APIRouter, Depends
from app.crud.descriptions import post, get_one, get_all
from app.schemas.descriptions import (
    DescriptionPayloadSchema,
    DescriptionResponseSchema,
    DescriptionSchema,
)

from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()


# This route should not be used as the post method is endeled by the scraper.
"""
@router.post("/", response_model=DescriptionResponseSchema, status_code=201)
async def create_description(
    payload: DescriptionPayloadSchema, db: Session = Depends(get_db)
) -> DescriptionResponseSchema:
    desription_id = await post(payload, db)

    response_object = {
        "layout": payload.layout,
        "brand": payload.brand,
        "product_type": payload.product_type,
        "profile": payload.profile,
        "layout_size": payload.layout_size,
        "layout_standard": payload.layout_standard,
        "layout_ergonomics": payload.layout_ergonomics,
        "hot_swappable": payload.hot_swappable,
        "knob_support": payload.knob_support,
        "rgb_support": payload.rgb_support,
        "display_support": payload.display_support,
        "qmk_via_support": payload.qmk_via_support,
        "connection": payload.connection,
        "battery_capacity": payload.battery_capacity,
        "mount_style": payload.mount_style,
        "case_material": payload.case_material,
        "keycap_material": payload.keycap_material,
    }

    return response_object
"""


@router.get("/{id}", response_model=DescriptionSchema)
async def read_one_description(
    id: int, db: Session = Depends(get_db)
) -> DescriptionSchema:
    description = await get_one(id, db)

    return description


@router.get("/", response_model=List[DescriptionSchema])
async def read_all_descriptions(
    db: Session = Depends(get_db),
) -> List[DescriptionSchema]:
    return await get_all(db)
