import os

import discord
from discord.ext import commands

from character_bot.message import Message


class Bot(commands.Bot):
    def __init__(self, name, prefix=None):
        intents = discord.Intents().default()
        intents.message_content = True
        super().__init__(command_prefix=prefix, intents=intents)
        self._name = name

    def get_name(self) -> str:
        return self._name

    async def send_message(self, message: Message):
        await super().get_channel(int(os.getenv("CHANNEL_ID"))).send(message.get_message_text())
