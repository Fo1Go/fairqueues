import os
from dataclasses import dataclass


@dataclass
class Settings:
    BOT_TOKEN: str = os.getenv('TG_BOT_API_KEY')


settings = Settings()
