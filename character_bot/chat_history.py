from typing import List

from message import Message


class ChatHistory:
    def __init__(self, messages: List[Message]):
        self._messages = messages

    def __next__(self) -> Message:
        for message in self._messages:
            yield message
