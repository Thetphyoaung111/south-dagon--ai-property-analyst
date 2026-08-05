from sqlalchemy import Column, Integer, String, Float
from app.database.database import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    township = Column(String, nullable=False)
    ward = Column(String, nullable=False)
    land_size = Column(String, nullable=False)
    document_type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    road = Column(String, nullable=True)
    phone = Column(String, nullable=True)