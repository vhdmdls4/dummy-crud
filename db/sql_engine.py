#connect_args = {"check_same_thread": False}
#engine = create_engine(sqlite_url, connect_args=connect_args)
from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

URL_DATABASE = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(URL_DATABASE, echo=True)

def get_db():
    with Session(engine) as session:
        yield session