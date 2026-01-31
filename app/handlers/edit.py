from aiogram import F, Router
from aiogram.types import Message

from app.keyboards.edit_configs import keyboard
from app.texts.buttons import ButtonText
from app.texts.templates import Messages

router = Router()


@router.message(F.text == ButtonText.SUBSCRIPTION_SETTINGS[1])
async def service_description(message: Message):
    await message.answer(text=Messages.SUBSCRIPTION_EDIT[3], reply_markup=keyboard)

