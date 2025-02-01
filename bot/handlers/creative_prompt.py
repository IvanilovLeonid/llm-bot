from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers.gigachat_generator import get_gigachat_response
from bot.utils.file_manager import get_one_user_interests


router = Router()

@router.message(Command("creative_prompt"))
async def creative_prompt(message: Message):
    user_id = message.from_user.id
    interests = get_one_user_interests(user_id)

    response = get_gigachat_response(
        system_message=f"Ты бот, который генерирует креативные задания на основе интересов пользователя: {interests}.",
        user_message="Подготовь креативное задание."
    )

    await message.reply(f"🎨 Креативное задание для вас: {response}")

