from aiogram import BaseMiddleware
from aiogram.types import Message
import csv

class RegistrationMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data: dict):
        user_id = event.from_user.id
        with open("data/users.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            if str(user_id) in [row[0] for row in reader]:
                if event.text.startswith("/start"):
                    await event.answer("Вы уже зарегистрированы!")
                    return
        return await handler(event, data)
