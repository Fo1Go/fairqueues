from aiogram import types
from aiogram.filters import Command
from .routers import router


@router.message(Command("start"))
async def start(
        message: types.Message
):
    await message.answer("Hi!")


