from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard_devices = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[6])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[7])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[8])],
        [KeyboardButton(text=ButtonText.BACK)]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

keyboard_pay = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[9])],
        [KeyboardButton(text=ButtonText.BACK)]
    ],

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

