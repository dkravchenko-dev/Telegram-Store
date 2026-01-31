from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard_devices = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[0])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[1])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[2])],
        [KeyboardButton(text=ButtonText.BACK)]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

keyboard_months = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[3])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[4])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[5])],
        [KeyboardButton(text=ButtonText.BACK)]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

keyboard_pay = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[6])],
        [KeyboardButton(text=ButtonText.BACK)]
    ],

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

keyboard_confirmation = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_SELECTION[7])],
        [KeyboardButton(text=ButtonText.BACK)]
    ],

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)
