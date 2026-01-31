from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText
from database.users_manager import user_search


async def keyboard_default(id_telegram, username):
    user = await user_search(id_telegram, username)

    if user['configs_count'] == 0:
        keyboard = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton(text=ButtonText.INITIAL_SELECTION[0])],
                [KeyboardButton(text=ButtonText.INITIAL_SELECTION[1])],
                [KeyboardButton(text=ButtonText.INITIAL_SELECTION[2])],
            ],

            resize_keyboard=True,
            input_field_placeholder='Выберите пункт в меню'
        )
    else:
        keyboard = ReplyKeyboardMarkup(
            keyboard = [
                [KeyboardButton(text=ButtonText.INITIAL_SELECTION[0])],
                [KeyboardButton(text=ButtonText.INITIAL_SELECTION[1])],
                [KeyboardButton(text=ButtonText.INITIAL_SELECTION[3])],
            ],

            resize_keyboard=True,
            input_field_placeholder='Выберите пункт в меню'
        )

    return keyboard
