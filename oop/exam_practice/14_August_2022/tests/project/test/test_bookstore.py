import unittest

from project.bookstore import Bookstore


class TestBookstore(unittest.TestCase):

    def setUp(self) -> None:
        self.store = Bookstore(10)

    def test_constructor(self):
        assert self.store.books_limit == 10
        assert self.store.availability_in_store_by_book_titles == {}
        assert self.store._Bookstore__total_sold_books == 0

    def test_total_sold_books_property(self):
        self.store._Bookstore__total_sold_books = 1
        assert self.store.total_sold_books == self.store._Bookstore__total_sold_books

    def test_books_limit_error_with_less_than_zero(self):
        with self.assertRaises(ValueError) as error:
            self.store.books_limit = -1
        assert str(error.exception) == "Books limit of -1 is not valid"

    def test_books_limit_error_with_zero(self):
        with self.assertRaises(ValueError) as error:
            self.store.books_limit = 0
        assert str(error.exception) == "Books limit of 0 is not valid"

    def test_len(self):
        self.store.availability_in_store_by_book_titles = {"first": 5, "second": 1}
        assert len(self.store) == 6

    def test_receive_book_limit_reached(self):
        self.store.availability_in_store_by_book_titles = {"first": 2, "second": 1}
        with self.assertRaises(Exception) as error:
            self.store.receive_book("first", 8)
        assert str(error.exception) == "Books limit is reached. Cannot receive more books!"

    def test_receive_book_successful(self):
        self.store.receive_book("book", 1)
        result = self.store.receive_book("book", 2)
        self.store.receive_book("another book", 3)
        assert self.store.availability_in_store_by_book_titles["book"] == 3
        assert result == "3 copies of book are available in the bookstore."

    def test_sell_book_doesnt_exist(self):
        with self.assertRaises(Exception) as error:
            self.store.sell_book("book", 2)
        assert str(error.exception) == "Book book doesn't exist!"

    def test_sell_book_not_enough(self):
        self.store.receive_book("book", 1)
        with self.assertRaises(Exception) as error:
            self.store.sell_book("book", 5)
        assert str(error.exception) == "book has not enough copies to sell. Left: 1"

    def test_sell_book_successful(self):
        self.store.receive_book("book", 4)
        result = self.store.sell_book("book", 4)
        assert result == "Sold 4 copies of book"
        assert self.store.total_sold_books == 4
        assert self.store.availability_in_store_by_book_titles["book"] == 0

    def test_str(self):
        self.store.receive_book("book", 3)
        self.store.receive_book("another book", 5)
        self.store.sell_book("book", 2)
        expected = f"Total sold books: 2\n" \
                   f"Current availability: 6\n" \
                   f" - book: 1 copies\n" \
                   f" - another book: 5 copies"
        assert str(self.store) == expected


if __name__ == '__main__':
    unittest.main()
