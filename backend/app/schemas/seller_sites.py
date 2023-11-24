from pydantic import BaseModel


class SellersitePayloadSchema(BaseModel):
    site_url: str
    site_name: str


class SellersiteResponseSchema(SellersitePayloadSchema):
    id: int
