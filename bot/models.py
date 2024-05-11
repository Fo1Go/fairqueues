from sqlalchemy import Column, Integer, String, Text, DateTime
from bot.utils.db import Base


class Roles(Base):
    id = Column()
    role = Column()


class User(Base):
    id = Column()
    username = Column()
    telegram_id = Column()
    time_created = Column()
    is_active = Column()
    role = Column()
    group = Column()


class Group(Base):
    id = Column()
    users = Column()
    name = Column()
    queues = Column()
    is_private = Column()


class Queue(Base):
    id = Column()
    description = Column()
    time_created = Column()
    time_started = Column()
    is_active = Column()
    activation_code = Column()
    group_id = Column()
    users = Column()
