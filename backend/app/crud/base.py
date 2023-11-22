from sqlalchemy.orm import Session

from app.models.keyboard import Keyboard
from app.schemas.hero_schema import *


def get_kb(db: Session, kb_id: int):
    return db.query(Keyboard).filter(Keyboard.id == kb_id).first()
