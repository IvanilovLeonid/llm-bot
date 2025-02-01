from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.utils.file_manager import save_to_csv
from aiogram.filters import Command
from datetime import datetime
from aiogram.fsm.state import State, StatesGroup


class RegistrationState(StatesGroup):
    name = State()
    interests = State()


router = Router()


@router.message(Command("start"))
async def start_registration(message: Message, state: FSMContext):
    state_data = await state.get_data()
    if state_data.get("registered"):
        await message.answer("Вы уже зарегистрированы!")
        return

    await message.answer("Привет! Данный бот служит для развития креативности. Для начала давайте зарегистрируемся. Как вас зовут?")
    await state.set_state(RegistrationState.name)


@router.message(RegistrationState.name)
async def ask_interests(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Спасибо! Теперь напишите ваши интересы через запятую (например, музыка, спорт, программирование):")
    await state.set_state(RegistrationState.interests)


@router.message(RegistrationState.interests)
async def save_data(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data.get("name")
    interests = message.text
    user_id = message.from_user.id
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    save_to_csv(user_id, name, interests, registration_date)

    await message.answer(f"Регистрация завершена, {name}! Спасибо, что поделились своими интересами. Вы можете использовать /menu для просмотра доступных команд.")
    await state.clear()


