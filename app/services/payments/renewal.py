from datetime import date, datetime

from aiogram.types import Message
from dateutil.relativedelta import relativedelta

from database.users_manager import user_search, user_update


async def after_payment(message: Message, id_telegram: int):
    user = await user_search(id_telegram)
    price = user.get("preliminary_price")
    subscription_end = user.get("preliminary_subscription_end")
    subscription_start = date.today()

    await user_update(id_telegram, "price", price)
    await user_update(id_telegram, "subscription_start", subscription_start.isoformat())
    await user_update(id_telegram, "subscription_end", subscription_end)


async def before_payment(message: Message, id_telegram: int, price: int, months: int):
    user = await user_search(id_telegram)
    subscription_end = user.get("subscription_end")

    if subscription_end:
        try:
            subscription_end = datetime.fromisoformat(str(subscription_end)).date()
        except ValueError:
            if isinstance(subscription_end, datetime):
                subscription_end = subscription_end.date()
            else:
                subscription_end = date.today()
    else:
        subscription_end = date.today()

    start_date = max(subscription_end, date.today())
    subscription_end_new = start_date + relativedelta(months=months)

    await user_update(id_telegram, "preliminary_price", price)
    await user_update(id_telegram, "preliminary_subscription_end", subscription_end_new.isoformat())
