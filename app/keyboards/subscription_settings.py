from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard_settings = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SETTINGS[0])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SETTINGS[1])],
        [KeyboardButton(text=ButtonText.BACK)]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)
