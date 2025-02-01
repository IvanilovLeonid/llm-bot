import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from bot.handlers import (
    brainstorm,
    creative_prompt,
    word_association,
    quote_of_the_day,
    challenge,
    feedback,
    menu,
    fallback,
    registration
)
from bot.middleware.registration_middleware import RegistrationMiddleware
from bot.middleware.logging_middleware import LoggingMiddleware
from bot.scheduler.scheduler import setup_scheduler

API_TOKEN = ""


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.update.outer_middleware(LoggingMiddleware())

    dp.message.middleware(RegistrationMiddleware())

    dp.include_router(brainstorm.router)
    dp.include_router(creative_prompt.router)
    dp.include_router(word_association.router)
    dp.include_router(quote_of_the_day.router)
    dp.include_router(challenge.router)
    dp.include_router(feedback.router)
    dp.include_router(registration.router)
    dp.include_router(menu.router)
    dp.include_router(fallback.router)
    setup_scheduler(bot)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

