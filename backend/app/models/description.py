from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

# peut etre import keybaord je ne suis pas sur
# from app.models.keyboard import Keyboard


class Description(Base):
    __tablename__ = "descriptions"

    id = Column(Integer, primary_key=True)
    layout = Column(String, nullable=True)
    brand = Column(String, nullable=True)
    product_type = Column(String, nullable=True)
    profile = Column(String, nullable=True)
    layout_size = Column(String, nullable=True)
    layout_standard = Column(String, nullable=True)
    layout_ergonomics = Column(String, nullable=True)
    hot_swappable = Column(String, nullable=True)
    knob_support = Column(Boolean, nullable=True)
    rgb_support = Column(Boolean, nullable=True)
    display_support = Column(Boolean, nullable=True)
    qmk_via_support = Column(Boolean, nullable=True)
    connection = Column(String, nullable=True)
    battery_capacity = Column(String, nullable=True)
    mount_style = Column(String, nullable=True)
    case_material = Column(String, nullable=True)
    keycap_material = Column(String, nullable=True)

    keyboard_id = Column(Integer, ForeignKey("keyboards.id"))
    keyboard = relationship(
        "Keyboard",
        back_populates="description",
        foreign_keys=[keyboard_id],
    )
