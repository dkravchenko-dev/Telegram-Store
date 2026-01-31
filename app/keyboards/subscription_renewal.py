from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_RENEWAL[0])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_RENEWAL[1])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_RENEWAL[2])],
        [KeyboardButton(text=ButtonText.BACK)]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

keyboard_pay = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_RENEWAL[3])],
        [KeyboardButton(text=ButtonText.BACK)]
    ],

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)
