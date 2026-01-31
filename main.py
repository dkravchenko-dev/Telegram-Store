import asyncio

from aiogram import Bot, Dispatcher

from app.config import TOKEN_BOT_USERS
from app.router import router

bot = Bot(token = TOKEN_BOT_USERS)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
#    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
