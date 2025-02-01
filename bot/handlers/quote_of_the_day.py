from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers.gigachat_generator import get_gigachat_response
from bot.utils.file_manager import get_one_user_interests
router = Router()


@router.message(Command("quote_of_the_day"))
async def quote_of_the_day(message: Message):
    user_id = message.from_user.id
    interests = get_one_user_interests(user_id)

    response = get_gigachat_response(
        system_message=f"Ты бот, который генерирует вдохновляющие цитаты для развития интересов: {interests}.",
        user_message="Подготовь вдохновляющую цитату."
    )

    await message.reply(f"💬 Цитата дня для вас: {response}")
