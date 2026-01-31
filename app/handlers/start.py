from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.layouts import keyboard_default
from app.texts.templates import Messages

router = Router()

@router.message(CommandStart())
async def start_bot(message: Message):
    id_telegram = message.from_user.id
    username = message.from_user.username or None

    keyboard = await keyboard_default(id_telegram, username)
    await message.answer(text=Messages.WELCOME, reply_markup=keyboard)
