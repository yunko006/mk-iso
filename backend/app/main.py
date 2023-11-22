import os

from fastapi import FastAPI


from app.api import ping

# from app.models.keyboard import Keyboard
# from sqlalchemy.orm import Session

from app.database import SessionLocal


def create_application() -> FastAPI:
    application = FastAPI()

    # add db here
    # declaration de la variable db pour mes autres routes.
    db = SessionLocal()

    # Test pour si ma connection est bonne.
    # def create_kb(db: Session):
    #     db_user = Keyboard(name="quatre", url="test", price=2)
    #     db.add(db_user)
    #     db.commit()
    #     db.refresh(db_user)
    #     return db_user

    # create_kb(db)
    # Fin de test.

    # api routes here
    application.include_router(ping.router)

    return application


app = create_application()
