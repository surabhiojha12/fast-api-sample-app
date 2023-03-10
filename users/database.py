from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Database configurations

# _user = os.environ.get('PGUSER')
# _password = os.environ.get('PGPASSWORD')
# _host = os.environ.get('PGHOST')
# _database = os.environ.get('PGDATABASE')
# _port = os.environ.get('PGPORT')

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
