from aiogram import F, Router
from aiogram.types import Message

from app.handlers.start import start_bot
from app.texts.buttons import ButtonText

router = Router()


@router.message(F.text == ButtonText.BACK)
async def server_instruction(message: Message):
    await start_bot(message)
