import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("SUPABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_db(testing: int = Depends(lambda x: Settings.testing)) -> Session:
#     if testing == 1:
#         db = sessionmaker(
#             autocommit=False, autoflush=False, bind=engine, schema="tests"
#         )
#     else:
#         db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
