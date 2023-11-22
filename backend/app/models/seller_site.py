from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base
from app.models.keyboard import Keyboard


class SellerSite(Base):
    __tablename__ = "seller_sites"

    site_id = Column(Integer, primary_key=True)
    site_name = Column(String)
    site_url = Column(String)

    keyboards = relationship("Keyboard", back_populates="seller_site")
