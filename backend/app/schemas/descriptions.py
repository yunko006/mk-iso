from pydantic import BaseModel
from typing import Optional


class DescriptionPayloadSchema(BaseModel):
    layout: str
    brand: str
    product_type: str
    profile: str
    layout_size: str
    layout_standard: str
    layout_ergonomics: str
    hot_swappable: Optional[bool]
    knob_support: Optional[bool]
    rgb_support: Optional[bool]
    display_support: Optional[bool]
    qmk_via_support: Optional[bool]
    connection: str
    battery_capacity: str
    mount_style: str
    case_material: str
    keycap_material: str
