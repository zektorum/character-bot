import asyncio

from character_bot.chat_history import ChatHistory


class BotManager:
    def __init__(self, chat_history: ChatHistory, *args):
        self._chat_history = chat_history
        self._bots = {}
        for bot in args:
            self._bots[bot.get_name()] = bot

    async def send_chat_history(self):
        message = self._chat_history.get_message()
        while message is not None:
            author = message.get_message_author()
            bot = self._bots[author]
            await asyncio.create_task(bot.send_message(message))
            message = self._chat_history.get_message()
