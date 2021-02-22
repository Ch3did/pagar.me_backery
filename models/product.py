from sqlalchemy import Column, Float, ForeignKey, Integer, String, Relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Product(Base):

    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable = False)
    store_id = Column(Integer, ForeignKey("store.store_id"), nullable=False)



class Store(Base):
    __tablename__ = "store"
    store_id = Column(Integer, primary_key=True)
    store_name = Column(String, nullable=False)
    cep = Column(Integer, nullable = False)



class Order(Base):

    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)
    total = Column(Float, nullable = False)
    adress = Column(String, nullable=False)
    id_prod = Column(Integer, ForeignKey("products.product_id"), nullable=False)
    name_user = Column(String, nullable=False)




    