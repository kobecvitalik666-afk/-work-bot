import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

TOKEN = "8910960847:AAFCo7Br7cbgpmK77mRAONcUNDpXZczvb2c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: Message):
    await msg.answer("Бот работает")

@dp.message()
async def echo(msg: Message):
    await msg.answer(msg.text)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
