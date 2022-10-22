import discord
from discord.ext import commands

from message import Message


class Bot(commands.Bot):
    def __init__(self, prefix=None):
        intents = discord.Intents().default()
        intents.message_content = True
        super().__init__(command_prefix=prefix, intents=intents)
        print("I was created")

    async def send_message(self, message: Message):
        print("In send_message")
        await super().get_channel(1028037599534780488).send(message.get_message_text())
