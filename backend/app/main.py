import os

from fastapi import FastAPI


from app.api import ping

from app.models.seller_site import SellerSite
from app.models.keyboard import Keyboard
from app.models.description import Description
from sqlalchemy.orm import Session

from app.database import SessionLocal


def create_application() -> FastAPI:
    application = FastAPI()

    # add db here
    # declaration de la variable db pour mes autres routes.
    db = SessionLocal()

    # Test pour si ma connection est bonne.
    # def create_seller_site(db: Session):
    #     kb = Keyboard(name="TEST42", url="url", price="5000", seller_site_id=4)
    #     db.add(kb)
    #     db.commit()
    #     db.refresh(kb)

    #     db_seller_site = SellerSite(
    #         site_name="EpoMakerERGRTEHG", site_url="https://epomaker.com/"
    #     )
    #     db.add(db_seller_site)
    #     db.commit()
    #     db.refresh(db_seller_site)
    #     return db_seller_site

    #     # db_description = Description(layout="ISO", keyboard_id=3)
    #     # db.add(db_description)
    #     # db.commit()
    #     # db.refresh(db_description)
    #     # return db_description

    # create_seller_site(db)
    # Fin de test.

    # api routes here
    application.include_router(ping.router)

    return application


app = create_application()
