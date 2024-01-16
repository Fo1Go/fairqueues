from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import URL
import os
from datetime import datetime


Base = declarative_base()
url = 'postgresql+psycopg2://postgres:postgres@db_postgres_c:5432/postgres'
engine = create_engine(url)
connection = engine.connect()


class TestModel(Base):
    """tablename: testingDB
    :param
    telegram_id: int
    name: string
    description: string
    """
    __tablename__: str = "testingDB"

    id = Column(Integer(), primary_key=True)
    telegram_id = Column(Integer(), nullable=False)
    date_creation = Column(DateTime(), default=datetime.now)
    date_last_update = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    name = Column(String(), nullable=False)
    description = Column(Text(), nullable=True)

    def __repr__(self):
        return f"Test({self.id}, {self.telegram_id}, {self.date_creation})"


def create_all_tables():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    create_all_tables()