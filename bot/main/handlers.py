from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from sqlalchemy.orm import sessionmaker
from models import TestModel, engine


session_instance = sessionmaker(bind=engine)
session = session_instance()
queue_router = Router()


@queue_router.message(Command("start"))
async def start(
        message: types.Message,
):
    await message.answer("Hi!")


@queue_router.message(Command("create"))
async def create_some(
        message: types.Message,
        command: types.BotCommand
):
    if command.args is None:
        await message.answer("Use arguments. Example: ")
        return
    if len(command.args.split(' ')) < 2:
        await message.answer("Don\'t enough arguments")
        return
    record = TestModel(
        name=command.args[0],
        telegram_id=message.from_user.id,
        description=command.args[1]
    )
    session.add(record)
    session.commit()
    await message.answer("Object has been created!")


@queue_router.message(Command("update"))
async def update_some(
        message: types.Message,
        command: types.BotCommand
):
    await message.answer("Hello!!!!!!!!!!")


@queue_router.message(Command("delete"))
async def delete_some(
        message: types.Message,
        command: types.BotCommand
):
    await message.answer("Hello!!!!!!!!!!")


@queue_router.message(Command("read"))
async def read_some(
        message: types.Message,
):
    record = session.query(TestModel).filter_by(telegram_id=message.from_user.id).all()
    await message.answer(f"{record}")
