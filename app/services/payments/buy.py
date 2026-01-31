from datetime import date, datetime

from aiogram.types import Message
from dateutil.relativedelta import relativedelta

from app.services.move_files import move_configs
from database.users_manager import user_search, user_update


async def after_payment(message: Message, id_telegram: int):
    user = await user_search(id_telegram)

    price = user.get("preliminary_price")
    devices = user.get("preliminary_configs_count")
    subscription_start = user.get("preliminary_subscription_start")
    subscription_end = user.get("preliminary_subscription_end")

    await user_update(id_telegram, "price", price)
    await user_update(id_telegram, "configs_count", devices)
    await user_update(id_telegram, "subscription_start", subscription_start)
    await user_update(id_telegram, "subscription_end", subscription_end)
    await move_configs("database/configs/conf", ".conf", id_telegram, devices)
    await move_configs("database/configs/png", ".png", id_telegram, devices)


async def before_payment(message: Message, id_telegram: int, price: int, devices: int, months: int):
    user = await user_search(id_telegram)
    subscription_start = date.today()
    subscription_end = subscription_start + relativedelta(months=months)
    subscription_end_user = user.get("subscription_end")

    if isinstance(subscription_end_user, str):
        subscription_end_user = datetime.fromisoformat(subscription_end_user)

    await user_update(id_telegram, "preliminary_price", price)
    await user_update(id_telegram, "preliminary_configs_count", devices)
    await user_update(id_telegram, "preliminary_subscription_start", subscription_start.isoformat())
    await user_update(id_telegram, "preliminary_subscription_end", subscription_end.isoformat())
