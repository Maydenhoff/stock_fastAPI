from config.database import Base
from sqlalchemy import Column, Integer, String,Float

class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    # client = 