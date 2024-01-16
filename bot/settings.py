import os
from dataclasses import dataclass


@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv('TG_BOT_API_KEY')
    ABSPATH: str = os.path.abspath(__file__)


settings = Settings()
