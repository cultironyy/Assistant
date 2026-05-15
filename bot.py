import asyncio
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# Загружаем переменные из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ Токен бота не найден. Проверь файл .env")

# Инициализируем бота и диспетчер
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("👋 Привет! Я простой бот.\nОтправь мне любое сообщение, и я его повторю.")

# Обработчик любых текстовых сообщений (эхо)
@dp.message()
async def echo_handler(message: Message):
    if message.text:
        await message.answer(f"🔁 Ты написал: {message.text}")

# Главная функция запуска
async def main():
    print("✅ Бот запущен и ожидает сообщений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())