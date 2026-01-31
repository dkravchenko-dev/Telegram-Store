import json
import asyncio

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramAPIError
from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup

from app.config import ID_ADMIN
from app.keyboards.admin_panel import keyboard
from app.texts.buttons import ButtonText
from app.texts.templates import Messages

router = Router()


@router.message(F.text == ButtonText.CONTROL_PANEL[1])
async def open_list_user(message: Message, bot: Bot):
    id_telegram = message.from_user.id

    if id_telegram == ID_ADMIN:
        with open("database/users.json", "r", encoding="utf-8") as f:
            users = json.load(f)

        for user in users:
            lines = [f"{k}: {v}" for k, v in user.items()]
            text = "\n".join(lines)
            await bot.send_message(chat_id=ID_ADMIN, text=f"<pre>{text}</pre>", parse_mode="HTML")


@router.message(F.text == ButtonText.CONTROL_PANEL[0])
async def open_admin_panel(message: Message, bot: Bot):
    id_telegram = message.from_user.id

    if id_telegram == ID_ADMIN:
        await bot.send_message(chat_id=ID_ADMIN, text=Messages.ADMINISTRATION[4], reply_markup=keyboard)

@router.message(F.text == ButtonText.PAYMENT_PROCESSING[4])
async def start_event(message: Message, bot: Bot):
    id_telegram = message.from_user.id
    #target_user_id = []
    # target_user_id = []


    keyboard = ReplyKeyboardMarkup(
        keyboard = [
            #          [KeyboardButton(text=ButtonText.SUBSCRIPTION_SETTINGS[0])],
            [KeyboardButton(text=ButtonText.BACK)]
        ],

        resize_keyboard=True,
        input_field_placeholder='Выберите пункт в меню'
    )


    if id_telegram == ID_ADMIN:
        for user_id in target_user_id:
            try:
                await bot.send_message(chat_id=user_id, text=Messages.EVENT, reply_markup=keyboard)
                await asyncio.sleep(0.1)  # Анти-флуд
                print(user_id)
            except TelegramAPIError as e:
                print(f"Не удалось отправить сообщение пользователю {user_id}: {e}")