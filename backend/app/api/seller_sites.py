from typing import List
from fastapi import APIRouter, HTTPException
from app.crud.seller_sites import post, get_one, get_all
from app.schemas.seller_sites import (
    SellersitePayloadSchema,
    SellersiteResponseSchema,
    SellerSiteSchema,
)


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


@router.get("/{id}/", response_model=SellerSiteSchema)
async def read_seller_site(id: int) -> SellerSiteSchema:
    seller_site = await get_one(id)

    return seller_site


@router.get("/", response_model=List[SellerSiteSchema])
async def read_all_seller_site() -> List[SellerSiteSchema]:
    return await get_all()
