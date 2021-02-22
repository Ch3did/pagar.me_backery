from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable = False)
    id_store = Column(Integer, ForeignKey("store.store_id"), nullable=False)



