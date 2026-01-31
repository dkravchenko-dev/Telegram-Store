from aiogram import F, Router
from aiogram.types import Message

from app.texts.buttons import ButtonText
from app.texts.templates import Messages

router = Router()


@router.message(F.text == ButtonText.INITIAL_SELECTION[0])
async def service_description(message: Message):
    await message.answer(text=Messages.SERVICE_DESCRIPTION)

