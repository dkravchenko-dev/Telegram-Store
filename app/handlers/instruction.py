from aiogram import F, Router
from aiogram.types import FSInputFile, InputMediaPhoto, Message

from app.keyboards.os import keyboard
from app.texts.buttons import ButtonText
from app.texts.templates import Messages

router = Router()

@router.message(F.text.in_([
    ButtonText.SYSTEM_SELECTION[0],
    ButtonText.SYSTEM_SELECTION[1],
    ButtonText.SYSTEM_SELECTION[2],
    ButtonText.SYSTEM_SELECTION[3],
]))
async def os_handler(message: Message):
    path = message.text
    
    media_group = [
        InputMediaPhoto(media=FSInputFile(f"app/img/{path}/0.png")),
        InputMediaPhoto(media=FSInputFile(f"app/img/{path}/1.png")),
        InputMediaPhoto(media=FSInputFile(f"app/img/{path}/2.png")),
        InputMediaPhoto(media=FSInputFile(f"app/img/{path}/3.png")),
        InputMediaPhoto(media=FSInputFile(f"app/img/{path}/4.png")),
    ]

    await message.answer_media_group(media=media_group)
    await message.answer(text=Messages.SERVICE_INSTRUCTION)


@router.message(F.text == ButtonText.INITIAL_SELECTION[1])
async def server_instruction(message: Message):
    await message.answer(text=Messages.INSTRUCTION, reply_markup=keyboard)
