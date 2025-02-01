from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("menu"))
async def menu(message: Message):
    commands = (
        "/start - Начать регистрацию\n"
        "/menu - Показать меню\n"
        "/brainstorm - Генерация идей\n"
        "/creative_prompt - Креативное задание\n"
        "/word_association - Ассоциации к слову\n"
        "/quote_of_the_day - Цитата дня\n"
        "/challenge - Креативный вызов\n"
        "/feedback - Оставить отзыв"
    )
    await message.answer(f"Доступные команды:\n{commands}")


