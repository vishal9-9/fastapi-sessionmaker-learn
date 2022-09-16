from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('mysql+pymysql://root:password@localhost/Database')
Session = sessionmaker(bind=engine)
Base = declarative_base()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
