import unittest

from project.library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self) -> None:
        self.library = Library("NL")

    def test_constructor(self):
        assert self.library.name == "NL"
        assert self.library.books_by_authors == {}
        assert self.library.readers == {}

    def test_name_error(self):
        with self.assertRaises(ValueError) as error:
            self.library.name = ""
        assert str(error.exception) == "Name cannot be empty string!"

    def test_add_book(self):
        self.library.add_book("Ivan", "Book")
        assert self.library.books_by_authors["Ivan"] == ["Book"]
        self.library.add_book("Ivan", "Another Book")
        assert self.library.books_by_authors["Ivan"] == ["Book", "Another Book"]

    def test_add_reader_successful(self):
        result = self.library.add_reader("Daniel")
        assert result is None
        assert self.library.readers["Daniel"] == []

    def test_add_reader_already_registered(self):
        self.library.add_reader("Daniel")
        result = self.library.add_reader("Daniel")
        assert len(self.library.readers) == 1
        assert result == "Daniel is already registered in the NL library."

    def test_rent_book_reader_not_registered(self):
        result = self.library.rent_book("Ivan", "Ivan", "Book")
        assert result == "Ivan is not registered in the NL Library."

    def test_rent_book_no_author_in_library(self):
        self.library.add_reader("Ivan")
        self.library.add_book("George", "Book")
        result = self.library.rent_book("Ivan", "Nikolai", "Book1")
        assert result == "NL Library does not have any Nikolai's books."

    def test_rent_book_no_book_from_author(self):
        self.library.add_reader("Ivan")
        self.library.add_book("George", "Book")
        result = self.library.rent_book("Ivan", "George", "Book1")
        assert result == """NL Library does not have George's "Book1"."""

    def test_rent_book_successful(self):
        self.library.add_reader("Ivan")
        self.library.add_book("George", "Book")
        self.library.add_book("George", "Book1")
        self.library.rent_book("Ivan", "George", "Book")
        assert self.library.readers["Ivan"] == [{"George": "Book"}]
        assert self.library.books_by_authors == {"George": ["Book1"]}


if __name__ == '__main__':
    unittest.main()
