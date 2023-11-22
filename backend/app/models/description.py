from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

# peut etre import keybaord je ne suis pas sur
from app.models.keyboard import Keyboard


class Description(Base):
    __tablename__ = "descriptions"

    description_id = Column(Integer, primary_key=True)
    layout = Column(String)
    brand = Column(String)
    product_type = Column(String)
    profile = Column(String)
    layout_size = Column(String)
    layout_standard = Column(String)
    layout_ergonomics = Column(String)
    hot_swappable = Column(Boolean)
    knob_support = Column(Boolean)
    rgb_support = Column(Boolean)
    display_support = Column(Boolean)
    qmk_via_support = Column(Boolean)
    connection = Column(String)
    battery_capacity = Column(String)
    mount_style = Column(String)
    case_material = Column(String)
    keycap_material = Column(String)

    keyboard_id = Column(Integer, ForeignKey("keyboards.keyboard_id"))
    keyboard = relationship("Keyboard", back_populates="description")
