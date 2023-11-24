from fastapi import APIRouter, HTTPException

from app.crud.seller_sites import post
from app.schemas.seller_sites import SellersitePayloadSchema, SellersiteResponseSchema


router = APIRouter()


@router.post("/", response_model=SellersiteResponseSchema, status_code=201)
async def create_seller_site(
    payload: SellersitePayloadSchema,
) -> SellersiteResponseSchema:
    seller_site_id = await post(payload)

    response_object = {
        "id": seller_site_id,
        "site_name": payload.site_name,
        "site_url": payload.site_url,
    }

    return response_object
