from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.texts.buttons import ButtonText

keyboard = ReplyKeyboardMarkup(
    keyboard = [
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[0])],
        [KeyboardButton(text=ButtonText.SUBSCRIPTION_EDIT[1])],
        [KeyboardButton(text=ButtonText.BACK)]
    ], 

    resize_keyboard=True,
    input_field_placeholder='Выберите пункт в меню'
)

