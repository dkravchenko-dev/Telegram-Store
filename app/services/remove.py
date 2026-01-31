import glob
import os

from aiogram.types import Message

from app.config import ID_ADMIN
from app.keyboards.back import keyboard_back
from app.services.move_files import move_configs
from app.texts.templates import Messages
from database.users_manager import user_search, user_update


async def confirm_configs(message: Message, id_telegram: int, devices: int):
    username = message.from_user.username or ''
    user = await user_search(id_telegram)
    devices_user = user.get("configs_count")
    new_count = devices_user - devices

    await user_update(id_telegram, "configs_count", new_count)
    await move_configs(f"database/configs/conf/{id_telegram}", ".conf", f"../trash/{id_telegram}", devices)
    await move_configs(f"database/configs/png/{id_telegram}", ".png", f"../trash/{id_telegram}", devices)

    files_trash = glob.glob(f"database/configs/conf/trash/{id_telegram}/*.conf")
    files_str = [os.path.basename(f) for f in files_trash]
    configs_count = ", ".join(files_str)
    reply_text = Messages.ADMINISTRATION[3].format(id_telegram=id_telegram, username=username, configs_count=configs_count)

    await message.bot.send_message(chat_id=ID_ADMIN, text=reply_text, reply_markup=keyboard_back)
    await message.answer(text=Messages.SUBSCRIPTION_EDIT[5], reply_markup=keyboard_back)

