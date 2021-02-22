from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Order(Base):

    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True)
    total = Column(Float, nullable = False)
    adress = Column(String, nullable=False)
    id_prod = Column(Integer, ForeignKey("product.product.id"), nullable=False)
    name_user = Column(String, nullable=False)



    

