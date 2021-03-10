#import libraries
from database.connection import engine
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base



#Base para os modelos
def model():
    Base = declarative_base()


    class Bakery(Base):
        __tablename__ = "bakeries"
        idbakery= Column(Integer, primary_key=True)
        user=Column(String(50))
        password=Column(String(50))
        name = Column(String(50))
        email=Column(String(50))
        cnpj=Column(Integer)
        city=Column(String(50))
        zipcode=Column(Integer)
        phone_number=Column(Integer)


    Base.metadata.create_all(engine)

    return '/'
