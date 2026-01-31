from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from app.texts.buttons import ButtonText
from database.users_manager import user_search


async def keyboard_configs(id_telegram: int) -> ReplyKeyboardMarkup:
    user = await user_search(id_telegram)
    configs_count = user.get("configs_count")

    builder = ReplyKeyboardBuilder()

    for i in range(configs_count):
        builder.add(KeyboardButton(text=f"{ButtonText.INITIAL_SELECTION[4]} {i+1}"))

    builder.adjust(*(2 for _ in range((configs_count + 1) // 2)))

    builder.row(
            KeyboardButton(text=ButtonText.INITIAL_SELECTION[5]),
            KeyboardButton(text=ButtonText.BACK)
    )

    return builder.as_markup(
            resize_keyboard=True,
            input_field_placeholder='Выберите пункт в меню'
    )
