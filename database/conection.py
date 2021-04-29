import sqlalchemy as db
from config  import typedb, host, user, password, database


def connection():
    try:
        engine = db.create_engine(typedb+"://"+user+":"+password+"@"+host+"/"+database)
        print(" * Database Conectada" )
        return engine
    except:
        print(' * Verifique as configurações dadatabase!   **')
        return None 

