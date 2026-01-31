from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message

from app.keyboards.remove_configs import keyboard_devices, keyboard_pay
from app.services.remove import confirm_configs
from app.texts.buttons import ButtonText
from app.texts.templates import Messages
from database.users_manager import user_search

router = Router()


class SubscribeForm(StatesGroup):
    additional_purchase = State()
    devices = State()


@router.message(F.text == ButtonText.SUBSCRIPTION_EDIT[9])
async def subscribe_pay(message: Message, state: FSMContext):
    id_telegram = message.from_user.id
    data = await state.get_data()
    devices = data.get("devices")

    if not devices:
        await message.answer(Messages.ERRORS[12])
        return

    await confirm_configs(message, id_telegram=id_telegram, devices=devices)
    await state.clear()


@router.message(F.text.in_([
    ButtonText.SUBSCRIPTION_EDIT[6],
    ButtonText.SUBSCRIPTION_EDIT[7],
    ButtonText.SUBSCRIPTION_EDIT[8],
]))
async def subscribe_devices(message: Message, state: FSMContext):
    data = await state.get_data()
    data.get("additional_purchase")
    
    id_telegram = message.from_user.id
    user = await user_search(id_telegram)


    try:
        devices = int(message.text.split()[0])
        devices_user = user.get("configs_count")
        old_price = devices_user * 50
        new_price = (devices_user - devices) * 50

        reply_text = Messages.SUBSCRIPTION_EDIT[4].format(devices=devices, old_price=old_price, new_price=new_price)
    except (IndexError, ValueError):
        await message.answer(Messages.ERRORS[4])
        return


    if devices_user <= 2:
        await message.answer(Messages.ERRORS[11])
        return

    if devices_user <= devices:
        await message.answer(Messages.ERRORS[13])
        return

    await message.answer(text=reply_text, reply_markup=keyboard_pay)
    await state.update_data(devices = devices)


@router.message(F.text == ButtonText.SUBSCRIPTION_EDIT[1])
async def increase_count(message: Message, state: FSMContext):
    await state.clear()
    
    await state.get_data()
    await state.update_data(additional_purchase=True)
    await message.answer(text=Messages.SUBSCRIPTION_EDIT[1], reply_markup=keyboard_devices)

