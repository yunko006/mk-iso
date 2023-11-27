# will use models.py for now, i'm considering a common folder to be share with api & scraper.

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# from app.models.seller_site import SellerSite
# from app.models.description import Description


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

    # description_id = Column(Integer, ForeignKey("descriptions.id"))
    description = relationship("Description", back_populates="keyboard")


class SellerSite(Base):
    __tablename__ = "seller_sites"

    id = Column(Integer, primary_key=True)
    site_name = Column(String, nullable=False)
    site_url = Column(String, nullable=False)

    # keyboard_id = Column(Integer, ForeignKey("keyboards.id"))
    keyboards = relationship("Keyboard", back_populates="seller_site")


class Description(Base):
    __tablename__ = "descriptions"

    id = Column(Integer, primary_key=True)
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

    keyboard_id = Column(Integer, ForeignKey("keyboards.id"))
    keyboard = relationship("Keyboard", back_populates="description")
