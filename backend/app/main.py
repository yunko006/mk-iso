import os

from fastapi import FastAPI


from app.api import ping


def create_application() -> FastAPI:
    application = FastAPI()

    # add db here

    # api routes here
    application.include_router(ping.router)

    return application


app = create_application()
