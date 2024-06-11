from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os
from dotenv import load_dotenv


import sqlalchemy

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")

load_dotenv(dotenv_path=env_path)

DATABASE_URL = sqlalchemy.engine.URL.create(
    drivername="mysql+pymysql",
    host="127.0.0.1",
    username=os.getenv("MARIADB_USER"),
    password=os.getenv("MARIADB_PASSWORD"),
    port=os.getenv("MARIADB_PORT"),
    database=os.getenv("MARIADB_DATABASE"),
)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully")