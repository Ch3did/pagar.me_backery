#import libraries
import json
from database.connection import engine, session
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class Bakery(Base):
    __tablename__ = "bakeries"
    idbakery= Column(Integer, primary_key=True, autoincrement=True)
    user=Column(String(50))
    password=Column(String(50))
    name = Column(String(50))
    email=Column(String(50))
    cnpj=Column(Integer)
    city=Column(String(50))
    zipcode=Column(Integer)
    phone_number=Column(Integer)



#Base para os modelos
def model():
    Base.metadata.create_all(engine)


def cadastro(jsn):
    dic = json.dumps(jsn) 
   
    cep = int(dic['cep'])
    cidade = dic['cidade']
    numero_tel = int(dic['numero_tel'])
    cnpj = int(dic['cnpj'])
    email = dic['email']
    nome = dic['nome']
    password = dic['password']
    user = dic['user']


    new_backery = Bakery(zipcode = cep, city = cidade, phone_number = numero_tel, cnpj = cnpj, email = email, name = nome, password = password, user = user)
    session.add(new_backery)
    session.commit()

def consulta():
    pass

