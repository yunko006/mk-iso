# will use models.py for now, i'm considering a common folder to be share with api & scraper.

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class Keyboard(Base):
    __tablename__ = "keyboards"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    url = Column(String)
    price = Column(Integer)
    image = Column(String, nullable=True)

    seller_site_id = Column(Integer, ForeignKey("seller_sites.id"))
    seller_site = relationship(
        "SellerSite",
        back_populates="keyboards",
    )

    description = relationship(
        "Description",
        back_populates="keyboard",
    )


class SellerSite(Base):
    __tablename__ = "seller_sites"

    id = Column(Integer, primary_key=True)
    site_name = Column(String, nullable=False)
    site_url = Column(String, nullable=False)

    keyboards = relationship("Keyboard", back_populates="seller_site")


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
