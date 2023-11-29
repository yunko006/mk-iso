from dataclasses import dataclass
from typing import Optional
from pydantic import BaseModel


@dataclass
class EpomakerScrapeResults:
    name: str
    url: str
    price: float
    image: Optional[str]
    seller_site_id: int = 2  # hardcode "2" pour simplifier pour le moment.


@dataclass
class KeychronScrapeResults:
    name: str
    url: str
    price: float
    image: Optional[str]
    seller_site_id: int = 67  # hardcode "2" pour simplifier pour le moment.


@dataclass
class DescriptionScrapeResults:
    layout: Optional[str]
    brand: Optional[str]
    product_type: Optional[str]
    profile: Optional[str]
    layout_size: Optional[str]
    layout_standard: Optional[str]
    layout_ergonomics: Optional[str]
    hot_swappable: Optional[bool]
    knob_support: Optional[bool]
    rgb_support: Optional[bool]
    display_support: Optional[bool]
    qmk_via_support: Optional[bool]
    connection: Optional[str]
    battery_capacity: Optional[str]
    mount_style: Optional[str]
    case_material: Optional[str]
    keycap_material: Optional[str]
