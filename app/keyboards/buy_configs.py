from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard_devices = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[2])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[3])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[4])],
        [KeyboardButton(text=ButtonText.BACK)]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

keyboard_pay = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[5])],
        [KeyboardButton(text=ButtonText.BACK)]
    ],

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)
