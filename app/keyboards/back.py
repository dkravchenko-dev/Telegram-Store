from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard_back = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text=ButtonText.BACK)
        ]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)
