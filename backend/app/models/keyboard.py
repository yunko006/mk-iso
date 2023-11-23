from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

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

    description = relationship("Description", back_populates="keyboard")
