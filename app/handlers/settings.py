from aiogram import F, Router
from aiogram.types import Message

from app.keyboards.subscription_settings import keyboard_settings
from app.texts.buttons import ButtonText
from app.texts.templates import Messages

router = Router()


@router.message(F.text == ButtonText.INITIAL_SELECTION[5])
async def subscription_settings(message: Message):
    await message.answer(text=Messages.SETTINGS, reply_markup=keyboard_settings)
