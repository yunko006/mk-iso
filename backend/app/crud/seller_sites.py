from typing import List, Union
from app.schemas.seller_sites import SellersitePayloadSchema
from app.models.seller_site import SellerSite
from app.database import SessionLocal


async def post(payload: SellersitePayloadSchema) -> int:
    seller_site = SellerSite(
        site_name=payload.site_name,
        site_url=payload.site_url,
    )

    db = SessionLocal()
    db.add(seller_site)
    db.commit()
    db.refresh(seller_site)
    return seller_site.id


async def get_one(id: int) -> Union[dict, None]:
    db = SessionLocal()
    query = db.query(SellerSite).filter(SellerSite.id == id).first()

    if query:
        return query
    return None


async def get_all() -> List:
    db = SessionLocal()
    seller_sites = db.query(SellerSite).all()
    return seller_sites
