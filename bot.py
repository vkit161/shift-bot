import os
from datetime import datetime, time
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram import F
import asyncio

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

DAY_START = time(14, 30)
DAY_END = time(18, 0)

NIGHT_START = time(20, 0)
NIGHT_END = time(23, 55)

def get_shift_type(now: time):
    if DAY_START <= now <= DAY_END:
        return "day"
    if NIGHT_START <= now <= NIGHT_END:
        return "night"
    return None

@dp.message(F.text.contains("НАЧАЛ"))
async def handle_start(msg: types.Message):
    now = datetime.now().time()
    shift = get_shift_type(now)

    if shift == "day":
        await msg.reply("Привет, заряду!")
    elif shift == "night":
        await msg.reply("Привет, заряду на ночь!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
