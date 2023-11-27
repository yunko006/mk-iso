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
