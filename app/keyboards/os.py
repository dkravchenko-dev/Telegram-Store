from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text=ButtonText.SYSTEM_SELECTION[0]),
            KeyboardButton(text=ButtonText.SYSTEM_SELECTION[1])
        ],

        [
            KeyboardButton(text=ButtonText.SYSTEM_SELECTION[2]),
            KeyboardButton(text=ButtonText.SYSTEM_SELECTION[3])
        ],

        [
            KeyboardButton(text=ButtonText.BACK)
        ]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

