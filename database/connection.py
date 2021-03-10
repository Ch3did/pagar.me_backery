from settings import DATABASE_CONFIG, ECHO
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(DATABASE_CONFIG, echo=ECHO)

Session = sessionmaker(bind=engine)


session = Session()