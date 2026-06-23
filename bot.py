import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = Your token was replaced with a new one. You can use this token to access HTTP API:
8910960847:AAFCo7Br7cbgpmK77mRAONcUNDpXZczvb2c

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handler(msg: types.Message):
    await msg.answer("Бот работает ✅")

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
