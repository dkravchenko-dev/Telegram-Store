from datetime import date, datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from babel.dates import format_date

from app.keyboards.buy_configs import keyboard_devices, keyboard_pay
from app.services.form_payment import payment
from app.texts.buttons import ButtonText
from app.texts.templates import Messages
from database.users_manager import user_search

router = Router()


class SubscribeForm(StatesGroup):
    additional_purchase = State()
    devices = State()
    price = State()


@router.message(F.text == ButtonText.SUBSCRIPTION_EDIT[5])
async def subscribe_pay(message: Message, state: FSMContext):
    id_telegram = message.from_user.id
    data = await state.get_data()
    devices = data.get("devices")
    price = data.get("price")

    if not devices:
        await message.answer(Messages.ERRORS[12])
        return

    await payment(message, "buy_configs", id_telegram=id_telegram, price=price, devices=devices)
    await state.clear()


@router.message(F.text.in_([
    ButtonText.SUBSCRIPTION_EDIT[2],
    ButtonText.SUBSCRIPTION_EDIT[3],
    ButtonText.SUBSCRIPTION_EDIT[4],
]))
async def subscribe_devices(message: Message, state: FSMContext):
    data = await state.get_data()
    additional_purchase = data.get("additional_purchase")

    id_telegram = message.from_user.id
    user = await user_search(id_telegram)

    date.today()
    date_obj = datetime.strptime(user['subscription_end'], "%Y-%m-%d")
    subscription_end = format_date(date_obj, "d MMMM y", locale="ru")
    today = datetime.today().date()
    days_left = (date_obj.date() - today).days
    days_left + 1

    if not additional_purchase:
        await message.answer(Messages.ERRORS[10])
        return

    try:
        devices = int(message.text.split()[0])
        price = (days_left / 30) * (devices * 50)
        price = round(price)

        devices_user = user.get("configs_count")
        old_price = devices_user * 50
        new_price = (devices_user + devices) * 50

        reply_text = Messages.SUBSCRIPTION_EDIT[2].format(configs_count=devices, price=price, old_price=old_price, new_price=new_price)
    except (IndexError, ValueError):
        await message.answer(Messages.ERRORS[4])
        return

    await message.answer(text=reply_text, reply_markup=keyboard_pay)
    await state.update_data(devices = devices, price = price)

@router.message(F.text == ButtonText.SUBSCRIPTION_EDIT[0])
async def increase_count(message: Message, state: FSMContext):
    await state.clear()
    
    await state.get_data()
    await state.update_data(additional_purchase=True)
    await message.answer(text=Messages.SUBSCRIPTION_EDIT[1], reply_markup=keyboard_devices)

