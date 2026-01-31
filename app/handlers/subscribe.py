from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from app.keyboards.subscription_form import (keyboard_devices, keyboard_months,
                                             keyboard_pay)
from app.services.form_payment import payment
from app.texts.buttons import ButtonText
from app.texts.templates import Messages

router = Router()


class SubscribeForm(StatesGroup):
    subscribe = State()
    devices = State()
    months = State()


@router.message(F.text == ButtonText.INITIAL_SELECTION[2])
async def subscribe(message: Message, state: FSMContext):
    await state.clear()
    await state.update_data(subscribe=subscribe)
    await message.answer(text=Messages.SUBSCRIBE[0], reply_markup=keyboard_devices)


@router.message(F.text.in_([
    ButtonText.SUBSCRIPTION_SELECTION[0],
    ButtonText.SUBSCRIPTION_SELECTION[1],
    ButtonText.SUBSCRIPTION_SELECTION[2],
]))
async def subscribe_devices(message: Message, state: FSMContext):
    data = await state.get_data()
    subscribe = data.get("subscribe")

    if not subscribe:
        await message.answer(Messages.ERRORS[0])
        return

    try:
        devices = int(message.text.split()[0])
    except (IndexError, ValueError):
        await message.answer(Messages.ERRORS[4])
        return

    await state.update_data(devices=devices)
    await message.answer(text=Messages.SUBSCRIBE[1], reply_markup=keyboard_months)


@router.message(F.text.in_([
    ButtonText.SUBSCRIPTION_SELECTION[3],
    ButtonText.SUBSCRIPTION_SELECTION[4],
    ButtonText.SUBSCRIPTION_SELECTION[5],
]))
async def subscribe_months(message: Message, state: FSMContext):
    data = await state.get_data()
    devices = data.get("devices")

    if not devices:
        await message.answer(Messages.ERRORS[2])
        return

    try:
        months = int(message.text.split()[0])
    except (IndexError, ValueError):
        await message.answer(Messages.ERRORS[3])
        return

    price = months * (devices * 50)
    await state.update_data(months=months)

    reply_text = Messages.SUBSCRIBE[2].format(price=price)
    await message.answer(text=reply_text, reply_markup=keyboard_pay)


@router.message(F.text == ButtonText.SUBSCRIPTION_SELECTION[6])
async def subscribe_pay(message: Message, state: FSMContext):
    data = await state.get_data()
    months = data.get("months")

    if not months:
        await message.answer(Messages.ERRORS[3])
        return

    devices = data.get("devices")
    months = data.get("months")
    price = months * (devices * 50)
    id_telegram = message.from_user.id

    if devices and months:
        await payment(message, "subscription_buy", id_telegram=id_telegram, price=price, devices=devices, months=months)
        await state.clear()
    else:
        await message.answer(Mesages.ERRORS[1])
