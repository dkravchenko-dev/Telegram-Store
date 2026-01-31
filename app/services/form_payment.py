import asyncio
from typing import Optional

from aiogram import F, Router
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)

from app.config import ID_ADMIN, SUPPORT_PROFILE
from app.keyboards.back import keyboard_back
from app.keyboards.subscription_form import keyboard_confirmation
from app.services.block_middleware import user_block
from app.texts.buttons import ButtonText
from app.texts.templates import Messages
from database.users_manager import user_clear_cache, user_search, user_update

from .payments import add, buy, renewal

router = Router()


@router.message(F.text.startswith(ButtonText.PAYMENT_PROCESSING[0]))
async def payment_rejections(message: Message):
    id_user = int(message.text.split('\n')[1].strip())
    id_telegram = message.from_user.id

    if id_telegram == ID_ADMIN:
        await user_update(id_user, "blacklist", True)
        await message.answer(text=Messages.ADMINISTRATION[2], reply_markup=keyboard_back)


@router.message(F.text.startswith(ButtonText.PAYMENT_PROCESSING[1]))
async def payment_acceptance(message: Message):
    id_telegram = message.from_user.id

    if id_telegram == ID_ADMIN:
        await message.answer(text=Messages.ADMINISTRATION[1], reply_markup=keyboard_back)


async def delay(message, id_telegram):
    await asyncio.sleep(5)

    user = await user_search(id_telegram)
    blacklist = await user_block(message, id_telegram)
    type_pay = user.get("preliminary_type_pay")

    if blacklist:
        return

    match type_pay:
        case "subscription_buy":
            await buy.after_payment(message, id_telegram)
        case "subscription_renewal":
            await renewal.after_payment(message, id_telegram)
        case "buy_configs":
            await add.after_payment(message, id_telegram)

    await user_clear_cache(id_telegram)
    await message.answer(text=Messages.SUBSCRIBE[5], reply_markup=keyboard_back)


@router.message(F.text == ButtonText.SUBSCRIPTION_SELECTION[7])
async def check(message: Message):
    id_telegram = message.from_user.id
    username = message.from_user.username or ''

    user = await user_search(id_telegram)
    price = user.get("preliminary_price")
    type_pay = user.get("preliminary_type_pay")
    reply_text = Messages.ADMINISTRATION[0].format(id_telegram=id_telegram, username=username, price=price)
    blacklist = user.get("blacklist")

    if type_pay == None:
        await message.bot.send_message(chat_id=id_telegram, text=Messages.ERRORS[0])
        return

    if blacklist:
        reply_text = Messages.BLOCKING.format(support_profile=SUPPORT_PROFILE)
        await message.bot.send_message(chat_id=id_telegram, text=reply_text)
        return

    payment_processing_text_0 = ButtonText.PAYMENT_PROCESSING[2].format(id_telegram=id_telegram)
    payment_processing_text_1 = ButtonText.PAYMENT_PROCESSING[3].format(id_telegram=id_telegram)

    keyboard_admin = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=payment_processing_text_1)],
            [KeyboardButton(text=payment_processing_text_0)],
        ],
        resize_keyboard=True,
        input_field_placeholder='Выберите пункт в меню'
    )

    await message.answer(text=Messages.SUBSCRIBE[4], reply_markup=ReplyKeyboardRemove())
    await message.bot.send_message(chat_id=ID_ADMIN, text=reply_text, reply_markup=keyboard_admin)
    await delay(message, id_telegram)


async def payment(
    message: Message,
    type_pay: str,
    id_telegram: int,
    price: int,
    devices: Optional[int] = None,
    months: Optional[int] = None
):
    reply_text = Messages.SUBSCRIBE[3].format(price=price)
    id_telegram = message.from_user.id
    user = await user_search(id_telegram)
    subscription_start = user.get("subscription_start")

    match type_pay:
        case "subscription_buy":
            if subscription_start is not None:
                await message.answer(text=Messages.ERRORS[5], reply_markup=keyboard_back)
                return

            await buy.before_payment(message, id_telegram, price, devices, months)
        case "subscription_renewal":
            if subscription_start is None:
                await message.answer(Messages.ERRORS[9], reply_markup=keyboard_back)
                return

            await renewal.before_payment(message, id_telegram, price, months)
        case "buy_configs":
            await add.before_payment(message, id_telegram, price, devices)

    await message.answer(text=reply_text)
    await user_update(id_telegram, "preliminary_type_pay", type_pay)
    await message.answer(text=Messages.PAYMENT_NUMBER, reply_markup=keyboard_confirmation)
