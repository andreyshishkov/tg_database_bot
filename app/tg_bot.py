import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from dotenv import load_dotenv

from config import TG_TOKEN
from llm.text2sql import transform_text_to_sql
from db import perform_sql_query

load_dotenv()

bot = Bot(token=TG_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Спроси меня что-нибудь о данных в базе данных, и я дам тебе ответ"
        )


@dp.message()
async def handle_query(message: types.Message):
    question = message.text

    sql_query = await transform_text_to_sql(question)
    result = await perform_sql_query(sql_query)

    await message.answer(str(result))


async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())