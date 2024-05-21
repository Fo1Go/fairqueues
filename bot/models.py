import datetime
from typing import List

from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import mapped_column, Mapped, relationship

from bot.utils.db import Base


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    code: Mapped[str] = mapped_column(nullable=True, unique=True)
    queues: Mapped[List["Queue"]] = relationship(back_populates="group")
    users = relationship()


class Roles(Base):
    __tablename__ = 'user_roles'

    id: Mapped[int] = mapped_column(primary_key=True)
    role: Mapped[str] = mapped_column(nullable=False)
    users: Mapped[List['User']] = relationship(back_populates='roles')


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(String(129), nullable=False)
    time_created: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True),
                                                            server_default=func.now())
    is_active: Mapped[bool] = mapped_column(default=True)
    roles: Mapped[List['Roles']] = relationship(back_populates='users')
    group: Mapped['Group'] = relationship(back_populates='users')


class Queue(Base):
    __tablename__ = 'queues'

    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str] = mapped_column(String(1024))
    time_created: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True),
                                                            server_default=func.now(),
                                                            default=func.now())
    time_started: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True),
                                                            server_default=func.now())
    is_active: Mapped[bool] = mapped_column(default=True)
    code: Mapped[str] = mapped_column(nullable=True, unique=True)
    group: Mapped["Group"] = relationship(back_populates="queues")
    users: Mapped[List["User"]] = relationship(back_populates="group")
