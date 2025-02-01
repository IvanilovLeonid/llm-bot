from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from bot.handlers.gigachat_generator import get_gigachat_response
from bot.utils.file_manager import get_one_user_interests
from aiogram.fsm.context import FSMContext


router = Router()


class FeedbackStates(StatesGroup):
    waiting_for_feedback = State()


@router.message(Command("feedback"))
async def feedback_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    interests = get_one_user_interests(user_id)

    await message.reply(f"Поделитесь своими креативными идеями, и я дам конструктивную обратную связь. Ваши интересы: {interests}")
    await state.set_state(FeedbackStates.waiting_for_feedback)


@router.message(FeedbackStates.waiting_for_feedback)
async def feedback_process(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_input = message.text
    interests = get_one_user_interests(user_id)

    response = get_gigachat_response(
        system_message=f"Ты бот, который дает обратную связь на основе интересов пользователя: {interests}.",
        user_message=user_input,
    )

    await message.answer(f"📈 Обратная связь по вашей идее с учётом интересов ({interests}):\n{response}")
    await state.clear()