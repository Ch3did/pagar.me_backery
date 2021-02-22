from sqlalchemy import create_engine
from order import Base
from product import Base
from store import Base

engine = create_engine("sqlite:///db.sqlite")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
