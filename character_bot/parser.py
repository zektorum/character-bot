from bs4 import BeautifulSoup

from typing import List

from character_bot.chat_history import ChatHistory
from character_bot.message import Message


class Parser:
    def __init__(self, html: str):
        self.html = html

    def get_messages(self) -> ChatHistory:
        authors = self._get_author_names()
        messages = self._get_messages_text()
        messages_list = []
        for author, message in zip(authors, messages):
            messages_list.append(Message(author, message))
        return ChatHistory(messages_list)

    def _get_author_names(self) -> List[str]:
        authors = []
        soup = BeautifulSoup(self.html, "html.parser")
        messages = soup.find_all(class_="default")
        author = ""
        for message in messages:
            soup = BeautifulSoup(str(message), "html.parser")
            previous_author = author
            author = str(soup.find(class_="from_name"))
            if author == "None":
                authors.append(previous_author)
                author = previous_author
            else:
                author = author.split("\n")[1]
                authors.append(author)
        return authors

    def _get_messages_text(self) -> List[str]:
        messages_list = []
        soup = BeautifulSoup(self.html, "html.parser")
        messages = soup.find_all(class_="default")
        current_message = ""
        for message in messages:
            soup = BeautifulSoup(str(message), "html.parser")
            previous_message = current_message
            current_message = str(soup.find(class_="text"))
            if current_message == "None":
                messages_list.append(previous_message)
            else:
                current_message = current_message.split("\n")[1]
                messages_list.append(self.replace_tg_symbols(self, current_message))
        return messages_list

    @staticmethod
    def replace_tg_symbols(self, text: str) -> str:
        return text.replace("&lt;", "<").replace("&gt;", ">").replace("<br/>", "\n").replace("*", "^")
