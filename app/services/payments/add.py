from aiogram.types import Message

from app.services.move_files import move_configs
from database.users_manager import user_search, user_update


async def after_payment(message: Message, id_telegram: int):
    user = await user_search(id_telegram)

    preliminary_price = user.get("preliminary_price")
    preliminary_devices = user.get("preliminary_configs_count")

    user_price = user.get("price")
    user_devices = user.get("configs_count")

    price = preliminary_price + user_price
    devices = preliminary_devices + user_devices

    await user_update(id_telegram, "price", price)
    await user_update(id_telegram, "configs_count", devices)
    await move_configs("database/configs/conf", ".conf", id_telegram, preliminary_devices)
    await move_configs("database/configs/png", ".png", id_telegram, preliminary_devices)

async def before_payment(message: Message, id_telegram: int, price: int, devices: int):
    await user_update(id_telegram, "preliminary_price", price)
    await user_update(id_telegram, "preliminary_configs_count", devices)
