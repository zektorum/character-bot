import asyncio
import os

import dotenv

from character_bot.bot import Bot
from character_bot.bot_manager import BotManager
from character_bot.parser import Parser


dotenv.load_dotenv()
first_bot = Bot(name=os.getenv("KIVY_NAME"), prefix="!")
second_bot = Bot(name=os.getenv("HORSE_NAME"), prefix="&")
third_bot = Bot(name=os.getenv("SPY_NAME"), prefix="%")


@second_bot.command()
async def start_dialog(ctx):
    html_doc = ""
    with open("messages.html", "r") as file:
        html_doc = "".join(file.read())
    chat_history = Parser(html_doc).get_messages()
    bot_manager = BotManager(chat_history, first_bot, second_bot, third_bot)
    await bot_manager.send_chat_history()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.create_task(first_bot.start(token=os.getenv("KIVY")))
    loop.create_task(second_bot.start(token=os.getenv("HORSE")))
    loop.create_task(third_bot.start(token=os.getenv("SPY")))

    loop.run_forever()
