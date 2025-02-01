from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Update
import csv

class LoggingMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):

        if isinstance(event, Update) and event.message:
            message = event.message
            user_id = message.from_user.id
            action = message.text

            try:
                with open("data/logs.csv", mode="a", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    writer.writerow([user_id, action])
            except Exception as e:
                print(f"Error while logging: {e}")

        return await handler(event, data)

