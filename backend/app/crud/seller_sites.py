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
