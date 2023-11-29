from pydantic import BaseModel
from typing import Optional


# Class not used in the api, see scraper.
class DescriptionPayloadSchema(BaseModel):
    layout: Optional[str]
    brand: Optional[str]
    product_type: Optional[str]
    profile: Optional[str]
    layout_size: Optional[str]
    layout_standard: Optional[str]
    layout_ergonomics: Optional[str]
    hot_swappable: Optional[str]
    knob_support: Optional[bool]
    rgb_support: Optional[bool]
    display_support: Optional[bool]
    qmk_via_support: Optional[bool]
    connection: Optional[str]
    battery_capacity: Optional[str]
    mount_style: Optional[str]
    case_material: Optional[str]
    keycap_material: Optional[str]


class DescriptionResponseSchema(BaseModel):
    id: int


class DescriptionBase(BaseModel):
    layout: Optional[str]
    brand: Optional[str]
    product_type: Optional[str]
    profile: Optional[str]
    layout_size: Optional[str]
    layout_standard: Optional[str]
    layout_ergonomics: Optional[str]
    hot_swappable: Optional[str]
    knob_support: Optional[bool]
    rgb_support: Optional[bool]
    display_support: Optional[bool]
    qmk_via_support: Optional[bool]
    connection: Optional[str]
    battery_capacity: Optional[str]
    mount_style: Optional[str]
    case_material: Optional[str]
    keycap_material: Optional[str]
    keyboard_id: int


class DescriptionSchema(DescriptionBase):
    id: int

    class config:
        from_attributes = True
