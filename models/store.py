from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Store(Base):

    __tablename__ = "store"

    store_id = Column(Integer, primary_key=True)
    store_name = Column(String, nullable=False)
    cep = Column(Integer, nullable = False)

