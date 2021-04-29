from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.orm import declarative_base
from database.conection import connection

Base = declarative_base()

class Backerys(Base):
    __tablename__ = 'Backerys'

    id_b = Column(Integer, primary_key=True)
    nome_b = Column(String(100), nullable=False)
    user = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)


class Products(Base):
    __tablename__ = 'Products'

    id_p = Column(Integer, primary_key=True)
    nome_B = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False) 
    qnt =  Column(Integer, nullable=False)


# class List(Base):
#     __tablename__ = 'Lista'

#     id_l = Column(Integer, primary_key=True)
#     products = relationship("Products", cascade="all, delete-orphan")
#     backerys = relationship("Backerys", cascade="all, delete-orphan")

if __name__ == "__main__":
    engine  = connection()
    Base.metadata.create_all(engine)