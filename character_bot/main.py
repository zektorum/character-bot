import asyncio
import os

import dotenv

from character_bot.bot import Bot
from character_bot.bot_manager import BotManager
from character_bot.chat_history import ChatHistory
from character_bot.file_reader import FileReader, ReadingMode
from character_bot.parser import Parser


dotenv.load_dotenv()

first_bot = Bot(name=os.getenv("KIVY_NAME"), prefix="!")
second_bot = Bot(name=os.getenv("HORSE_NAME"), prefix="&")
third_bot = Bot(name=os.getenv("SPY_NAME"), prefix="%")


@second_bot.command()
async def start_dialogue(ctx):
    fl = None
    if len(ctx.message.attachments) == 0 and os.path.exists("messages.html"):
        fl = FileReader(ReadingMode.SINGLE_FILE, filename="messages.html")
    elif len(ctx.message.attachments) == 0 and os.path.exists("messages/"):
        fl = FileReader(ReadingMode.MULTIPLE_FILES, messages_count=len(os.listdir("messages/")))
    elif len(ctx.message.attachments) == 1:
        fl = FileReader(ReadingMode.FROM_ATTACHMENT, attachment_url=ctx.message.attachments[0].url)
    html_doc = fl.read()
    chat_history = None
    if type(html_doc) == str:
        chat_history = Parser(html_doc).get_messages()
    elif type(html_doc) == list:
        chat_history = ChatHistory([])
        i = 0
        with open("bot.log", "a") as log:
            for page in html_doc:
                log.write(f"parsing page {i}\n")
                log.flush()
                for message in Parser(page).get_messages().messages:
                    chat_history.messages.append(message)
                i += 1
    bot_manager = BotManager(chat_history, first_bot, second_bot, third_bot)
    await bot_manager.send_chat_history()


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.create_task(first_bot.start(token=os.getenv("KIVY")))
    loop.create_task(second_bot.start(token=os.getenv("HORSE")))
    loop.create_task(third_bot.start(token=os.getenv("SPY")))

    loop.run_forever()
