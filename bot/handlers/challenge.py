from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers.gigachat_generator import get_gigachat_response
from bot.utils.file_manager import get_one_user_interests

router = Router()


@router.message(Command("challenge"))
async def creative_challenge(message: Message):
    user_id = message.from_user.id
    interests = get_one_user_interests(user_id)

    response = get_gigachat_response(
        system_message=f"Ты бот, который генерирует креативные вызовы на основе интересов пользователя: {interests}.",
        user_message="Подготовь креативный вызов на день или неделю."
    )

    await message.reply(f"🎯 Ваш креативный вызов: {response}")