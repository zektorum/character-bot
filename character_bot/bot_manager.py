import asyncio

from character_bot.chat_history import ChatHistory


class BotManager:
    def __init__(self, chat_history: ChatHistory, *args):
        self._chat_history = chat_history
        self._bots = {}
        for bot in args:
            self._bots[bot.get_name()] = bot

    async def send_chat_history(self):
        messages_count = len(self._chat_history.messages)
        with open("bot.log", "a") as log:
            log.write(f"messages for sending: {messages_count}\n")
            log.flush()
        message = self._chat_history.get_message()
        i = 0
        while message is not None:
            if i % 100 == 0:
                with open("bot.log", "a") as log:
                    log.write(f"messages sended: {i}/{messages_count - i}\n")
                    log.flush()
            author = message.get_message_author()
            bot = self._bots[author]
            await asyncio.create_task(bot.send_message(message))
            message = self._chat_history.get_message()
            i += 1
