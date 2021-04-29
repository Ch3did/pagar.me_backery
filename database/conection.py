import sqlalchemy as db
from config  import type, host, user, password, database


def connection():
    try:
        engine = db.create_engine(type+"://"+user+":"+password+"@"+host+"/"+database)
        return engine
    except:
        print (" * Verifique as configurações dadatabase")
        return null 

