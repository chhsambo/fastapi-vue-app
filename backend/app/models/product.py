from sqlalchemy import *
from app.db import Base


class Product(Base):
    __tablename__ = "products"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR, unique=True)
    price = Column(DECIMAL)
