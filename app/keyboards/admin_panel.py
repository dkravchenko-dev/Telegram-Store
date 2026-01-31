from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.CONTROL_PANEL[1])],
        [KeyboardButton(text=ButtonText.CONTROL_PANEL[2])],
        [KeyboardButton(text=ButtonText.CONTROL_PANEL[3])],
        [KeyboardButton(text=ButtonText.CONTROL_PANEL[4])],
        [KeyboardButton(text=ButtonText.BACK)]
    ],

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)
