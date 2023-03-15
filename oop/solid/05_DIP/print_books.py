from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Format(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class Formatter(Format):
    def format(self, book: Book) -> str:
        return book.content


class Printer:

    def __init__(self, formatter: Format):
        self.formatter = formatter

    def get_book(self, book: Book, ):
        formatted_book = self.formatter.format(book)
        return formatted_book
