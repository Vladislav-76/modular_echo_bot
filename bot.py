import asyncio

from aiogram import Bot, Dispatcher
from config_data import config


async def main() -> None:
    bot = Bot(token=config.token)
    admin_ids = config.admin_ids
    dp = Dispatcher()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
