#config.py

import os
from dotenv import load_dotenv # type: ignore

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "MyDummyCrud 🔥"
    PROJECT_VERSION: str = "1.0.0"

    DB_USERNAME : str = os.getenv("POSTGRES_USER")
    DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    DB_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    DB_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{POSTGRES_DB}"

settings = Settings()