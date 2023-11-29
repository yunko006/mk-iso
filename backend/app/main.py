import os

from fastapi import FastAPI


from app.api import ping, seller_sites, keyboards, descriptions


def create_application() -> FastAPI:
    application = FastAPI()
    # db = SessionLocal()

    # api routes here
    application.include_router(ping.router)
    application.include_router(
        seller_sites.router, prefix="/seller_sites", tags=["seller_sites"]
    )
    application.include_router(
        keyboards.router, prefix="/keyboards", tags=["keyboards"]
    )
    application.include_router(
        descriptions.router, prefix="/descriptions", tags=["descriptions"]
    )
    return application


app = create_application()
