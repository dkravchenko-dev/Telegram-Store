from aiogram import F, Router
from aiogram.types import Message

from app.keyboards.subscription_renewal import keyboard, keyboard_pay
from app.services.form_payment import payment
from app.texts.buttons import ButtonText
from app.texts.templates import Messages
from database.users_manager import user_search, user_update

router = Router()


@router.message(F.text == ButtonText.SUBSCRIPTION_RENEWAL[3])
async def subscribe_pay(message: Message):
    id_telegram = message.from_user.id
    user = await user_search(id_telegram)
    devices = user.get("configs_count")
    months = user.get("preliminary_subscription_end")

    if months is None:
        await message.answer(Messages.ERRORS[3])
        return

    price = months * (devices * 50)
    await payment(message, "subscription_renewal", id_telegram=id_telegram, price=price, months=months)


@router.message(F.text == ButtonText.SUBSCRIPTION_RENEWAL[0])
async def subscription_renewal_1(message: Message):
    id_telegram = message.from_user.id
    await subscription_renewal_months(message, id_telegram, 1)


@router.message(F.text == ButtonText.SUBSCRIPTION_RENEWAL[1])
async def subscription_renewal_2(message: Message):
    id_telegram = message.from_user.id
    await subscription_renewal_months(message, id_telegram, 2)


@router.message(F.text == ButtonText.SUBSCRIPTION_RENEWAL[2])
async def subscription_renewal_3(message: Message):
    id_telegram = message.from_user.id
    await subscription_renewal_months(message, id_telegram, 3)


async def subscription_renewal_months(message: Message, id_telegram: int, months: int):
    user = await user_search(id_telegram)
    devices = user.get("configs_count")
    price = months * (devices * 50)
    reply_text = Messages.SUBSCRIPTION_RENEWAL[1].format(price=price)

    await user_update(id_telegram, "preliminary_subscription_end", months)
    await message.answer(text=reply_text, reply_markup=keyboard_pay)


@router.message(F.text == ButtonText.SUBSCRIPTION_SETTINGS[0])
async def subscription_renewal(message: Message):
    await message.answer(text=Messages.SUBSCRIPTION_RENEWAL[0], reply_markup=keyboard)
