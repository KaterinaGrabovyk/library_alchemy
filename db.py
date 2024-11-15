from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dbUrl = "sqlite:///library.db"
engine = create_engine(dbUrl)

db = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)