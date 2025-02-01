from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from aiogram.filters import Command
from bot.handlers.gigachat_generator import get_gigachat_response
from bot.utils.file_manager import get_one_user_interests
from aiogram.fsm.context import FSMContext
router = Router()


class WordAssociationStates(StatesGroup):
    waiting_for_word = State()


@router.message(Command("word_association"))
async def word_association_start(message: Message, state: FSMContext):
    user_id = message.from_user.id
    interests = get_one_user_interests(user_id)

    await message.reply(f"Введите слово, и я подберу ассоциации. Ваши интересы: {interests}")
    await state.set_state(WordAssociationStates.waiting_for_word)


@router.message(WordAssociationStates.waiting_for_word)
async def word_association_process(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_input = message.text
    interests = get_one_user_interests(user_id)

    response = get_gigachat_response(
        system_message=f"Ты бот, который генерирует ассоциации на основе интересов пользователя: {interests}.",
        user_message=user_input,
    )

    await message.answer(f"🔑 Ассоциации по слову '{user_input}' с учётом ваших интересов ({interests}):\n{response}")
    await state.clear()