from pydantic import BaseModel


class SellersitePayloadSchema(BaseModel):
    site_url: str
    site_name: str


class SellersiteResponseSchema(SellersitePayloadSchema):
    id: int


class SellerSiteBase(BaseModel):
    site_name: str
    site_url: str


class SellerSiteSchema(SellerSiteBase):
    id: int

    class Config:
        from_attributes = True
