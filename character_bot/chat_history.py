from collections import deque
from typing import List

from character_bot.message import Message


class ChatHistory:
    def __init__(self, messages: List[Message]):
        self.messages = deque(messages)
        messages.clear()

    def get_message(self):
        if len(self.messages) != 0:
            return self.messages.popleft()
        return None

    def __str__(self):
        result = "['"
        for i in range(len(self.messages)):
            result += self.messages.__getitem__(i).get_message_text() + "', "
        return result[:-2] + "]"
