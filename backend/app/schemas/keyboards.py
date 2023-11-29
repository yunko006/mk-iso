from typing import Optional
from pydantic import BaseModel
from app.schemas.descriptions import DescriptionPayloadSchema


class KeyboardPayloadSchema(BaseModel):
    name: str
    url: str
    price: int
    image: Optional[str]
    seller_site_id: int
    description_id: int


class KeyboardResponseSchema(KeyboardPayloadSchema):
    id: int


class KeyboardBase(BaseModel):
    name: str
    url: str
    price: int
    seller_site_id: int
    image: Optional[str]


class KeyboardSchema(KeyboardBase):
    id: int

    class config:
        from_attributes = True
