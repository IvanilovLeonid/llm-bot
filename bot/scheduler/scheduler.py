from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.utils.file_manager import get_user_interests
from bot.handlers.gigachat_generator import generate_motivation

async def send_notifications(bot: Bot):
    users = get_user_interests()
    for user in users:
        user_id = user["user_id"]
        interests = user["interests"]
        try:
            motivation = generate_motivation(interests)
            await bot.send_message(user_id, f"🔔 Мотивация для вас:\n{motivation}")
        except Exception as e:
            print(f"Ошибка отправки сообщения пользователю {user_id}: {e}")


def setup_scheduler(bot):

    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_notifications, "interval", minutes=3, args=[bot])
    scheduler.start()