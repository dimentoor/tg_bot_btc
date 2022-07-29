import requests
from datetime import datetime
import json
# подключаем файл с токеном
from auth_data import tg_bot_token

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hello friend! Write the 'price' to find out the cost of BTC!")


@dp.message_handler()
async def send_text(message: types.Message):
    if message.text.lower() == "price":
        try:
            req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
            response = req.json()

            with open('1_help_file.json', 'w') as file:
                json.dump(response, file, indent=4, ensure_ascii=False)

            sell_price = response["btc_usd"]["sell"]
            await message.reply(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell BTC price: {sell_price}")

        except:
            await message.reply("Damn...Something was wrong...")
    else:
        await message.reply("Whaaat??? Check the command dude!")


if __name__ == '__main__':
    # get_data()
    executor.start_polling(dp)

