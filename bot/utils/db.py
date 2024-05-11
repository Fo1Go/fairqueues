from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.engine import URL, create_engine
from bot.settings import settings


class Base(DeclarativeBase):
    ...


url = URL.create(drivername=settings.DB_DRIVER_NAME,
                 username=settings.DB_USERNAME,
                 password=settings.DB_PASSWORD,
                 host=settings.DB_HOST,
                 port=settings.DB_PORT,
                 database=settings.DB_DATABASE)
engine = create_engine(url)
connection = engine.connect()

maker = sessionmaker(bind=engine)
session = maker()
