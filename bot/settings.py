import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv(".environment")


@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv('TG_BOT_API_KEY')
    ABSPATH: str = os.path.abspath(__file__)
    DB_DRIVER_NAME: str = os.getenv("POSTGRES_DRIVER_NAME")
    DB_USERNAME: str = os.getenv("POSTGRES_USERNAME")
    DB_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    DB_HOST: str = os.getenv("POSTGRES_HOST")
    DB_PORT: str = os.getenv("POSTGRES_PORT")


settings = Settings()
