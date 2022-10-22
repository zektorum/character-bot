class Message:
    def __init__(self, author: str, text: str):
        self._author = author
        self._text = text

    def get_message_text(self) -> str:
        return self._text

    def get_message_author(self) -> str:
        return self._author

    def __str__(self):
        return f"{self._author}: {self._text}"
