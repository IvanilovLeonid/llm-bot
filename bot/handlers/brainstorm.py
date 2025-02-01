from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers.gigachat_generator import get_gigachat_response
from bot.utils.file_manager import get_one_user_interests
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class BrainstormState(StatesGroup):
    waiting_for_topic = State()


@router.message(Command("brainstorm"))
async def brainstorm_start(message: Message, state: FSMContext):
    """Обработчик команды /brainstorm"""
    user_id = message.from_user.id

    interests = get_one_user_interests(user_id)
    if interests == "не указаны":
        await message.answer("Вам лучше зарегестрироваться, ведь без регистрации советы бота будут менее эффективными")

    await state.set_state(BrainstormState.waiting_for_topic)
    await message.reply(
        f"Введите тему или проблему для мозгового штурма. Ваши интересы: {interests}"
    )


@router.message(BrainstormState.waiting_for_topic)
async def brainstorm_generate(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    user_input = msg.text
    interests = get_one_user_interests(user_id)

    response = get_gigachat_response(
        system_message=f"Ты бот, который генерирует идеи на основе пользовательских интересов: {interests}.",
        user_message=user_input,
    )

    await msg.answer(
        f"💡 Идеи по теме '{user_input}' с учётом ваших интересов ({interests}):\n{response}"
    )

    await state.clear()
