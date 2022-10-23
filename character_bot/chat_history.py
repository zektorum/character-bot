from collections import deque
from typing import List

from message import Message


class ChatHistory:
    def __init__(self, messages: List[Message]):
        self._messages = deque(messages)

    def get_message(self) -> Message:
        return self._messages.popleft()

    def __str__(self):
        result = "['"
        for i in range(len(self._messages)):
            result += self._messages.__getitem__(i).get_message_text() + "', "
        return result[:-2] + "]"
