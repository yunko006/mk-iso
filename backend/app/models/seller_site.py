from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

# from app.models.keyboard import Keyboard


class SellerSite(Base):
    __tablename__ = "seller_sites"

    id = Column(Integer, primary_key=True)
    site_name = Column(String, nullable=False)
    site_url = Column(String, nullable=False)

    # keyboard_id = Column(Integer, ForeignKey("keyboards.id"))
    keyboards = relationship("Keyboard", back_populates="seller_site")
