import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from handlers import start_router, menu_router

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
    if not BOT_TOKEN or BOT_TOKEN == "your_token_here":
        raise ValueError(
            "BOT_TOKEN не найден или не заполнен. "
            "Откройте файл .env и вставьте туда токен, полученный у @BotFather."
        )

    logging.basicConfig(level=logging.INFO)

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(menu_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
