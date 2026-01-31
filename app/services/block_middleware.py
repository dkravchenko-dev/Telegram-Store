from app.config import SUPPORT_PROFILE
from app.texts.templates import Messages
from database.users_manager import user_search


async def user_block(message, id_telegram: int):
    user = await user_search(id_telegram)
    blacklist = user.get("blacklist") 

    if blacklist == True:
        reply_text = Messages.BLOCKING.format(support_profile=SUPPORT_PROFILE) 
        await message.bot.send_message(chat_id=id_telegram, text=reply_text)
        return True

    return False
