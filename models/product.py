from config.database import Base
from sqlalchemy import Column, Integer, String,Float

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key = True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)

