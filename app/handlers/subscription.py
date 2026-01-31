import os
import re
import tempfile
from datetime import datetime

from aiogram import F, Router
from aiogram.types import FSInputFile, Message
from babel.dates import format_date
from PIL import Image

from app.keyboards.back import keyboard_back
from app.keyboards.subscription_view import keyboard_configs
from app.services.block_middleware import user_block
from app.texts.buttons import ButtonText
from app.texts.templates import Messages
from database.users_manager import user_search

router = Router()

@router.message(F.text.regexp(fr"^{ButtonText.INITIAL_SELECTION[4]} \d+$"))
async def config(message: Message):
    id_telegram = message.from_user.id
    user = await user_search(id_telegram)
    blacklist = await user_block(message, id_telegram)

    if blacklist:
        return

    if datetime.fromisoformat(user.get("subscription_end")) < datetime.now():
        await message.answer(Messages.ERRORS[8])
        return

    conf_index = int(re.search(fr"{ButtonText.INITIAL_SELECTION[4]} (\d+)", message.text).group(1)) - 1
    conf_folder = f"database/configs/conf/{id_telegram}/"
    png_folder = f"database/configs/png/{id_telegram}/"

    if not os.path.exists(conf_folder) or not os.path.exists(png_folder):
        await message.answer(Messages.ERRORS[6])
        return

    conf_files = sorted([
        f for f in os.listdir(conf_folder)
        if os.path.isfile(os.path.join(conf_folder, f)) and f.endswith(".conf")
    ])

    png_files = sorted([
        f for f in os.listdir(png_folder)
        if os.path.isfile(os.path.join(png_folder, f)) and f.lower().endswith(".png")
    ])

    if conf_index < 0 or conf_index >= len(conf_files) or conf_index >= len(png_files):
        await message.answer(Messages.ERRORS[7])
        return

    conf_file_path = os.path.join(conf_folder, conf_files[conf_index])
    png_file_path = os.path.join(png_folder, png_files[conf_index])

    try:
        with Image.open(png_file_path) as im:
            if im.mode in ("RGBA", "LA"):
                background = Image.new("RGB", im.size, (255, 255, 255))
                background.paste(im, mask=im.split()[3])
            else:
                background = im.convert("RGB")

            with tempfile.TemporaryDirectory() as tmpdir:
                temp_path = os.path.join(tmpdir, os.path.basename(png_file_path))
                background.save(temp_path, "PNG")
                await message.answer_document(document=FSInputFile(temp_path))
    except Exception as e:
        print("Ошибка обработки PNG:", e)
        await message.answer("Ошибка при обработке изображения.")
        return

    try:
        with open(conf_file_path, "r", encoding="utf-8") as f:
            conf_text = f.read()
        await message.answer(text=conf_text)
    except Exception as e:
        print("Ошибка чтения конфига:", e)
        await message.answer("Ошибка при чтении конфигурационного файла.")


@router.message(F.text == ButtonText.INITIAL_SELECTION[3])
async def subscription(message: Message):
    id_telegram = message.from_user.id
    blacklist = await user_block(message, id_telegram)

    
    #if id_telegram == ID_ADMIN:
    #    id_telegram = 6503546806

    user = await user_search(id_telegram)
    keyboard = await keyboard_configs(id_telegram)
    configs_count = user['configs_count']

    if configs_count == 0:
        await message.answer(Messages.ERRORS[0], reply_markup=keyboard_back)
        return
    
    if blacklist:
        return

    date_obj = datetime.strptime(user['subscription_end'], "%Y-%m-%d")
    subscription_end = format_date(date_obj, "d MMMM y", locale="ru")
    today = datetime.today().date()
    days_left = (date_obj.date() - today).days
    days_left + 1

    reply_text = Messages.SUBSCRIPTION.format(
        configs_count=configs_count,
        subscription_end=subscription_end,
        days_left=days_left
    )

    await message.answer(text=reply_text, reply_markup=keyboard)

