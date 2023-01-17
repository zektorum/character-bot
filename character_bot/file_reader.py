from enum import Enum
from typing import List

import requests


class ReadingMode(Enum):
    SINGLE_FILE = 0
    MULTIPLE_FILES = 1
    FROM_ATTACHMENT = 2


class FileReader:
    def __init__(self, reading_mode: ReadingMode, **kwargs):
        self.reading_mode = reading_mode
        self.filename = kwargs.get("filename")
        self.messages_count = kwargs.get("messages_count")
        self.attachment_url = kwargs.get("attachment_url")

    def read(self) -> str | List[str]:
        if self.reading_mode == ReadingMode.SINGLE_FILE:
            with open(self.filename, "r") as file:
                return "".join(file.read())
        elif self.reading_mode == ReadingMode.MULTIPLE_FILES:
            html_data = []
            with open("messages/messages.html") as file:
                html_data.append("".join(file.read()))
            with open("bot.log", "a") as log:
                for i in range(2, self.messages_count + 1):
                    log.write(f"read file {i}\n")
                    log.flush()
                    with open(f"messages/messages{i}.html", "r") as file:
                        html_data.append("".join(file.read()))
            return html_data
        elif self.reading_mode == ReadingMode.FROM_ATTACHMENT:
            response = requests.get(self.attachment_url)
            response.encoding = "utf-8"
            return response.text
