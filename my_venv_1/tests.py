'''
ТЕСТЫ,

по основному функционалу

'''
import os
import unittest
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Book1", "Author1", 2000)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        self.library.add_book("Book1", "Author1", 2000)
        book_id = max(self.library.books.keys())
        self.library.remove_book(book_id)
        self.assertNotIn(book_id, self.library.books)

    def test_search_book(self):
        self.library.add_book("Book1", "Author1", 2000)
        self.library.add_book("Book2", "Author2", 2005)
        found_books = self.library.search_book("Book1")
        self.assertEqual(len(found_books), 1)
        self.assertEqual(found_books[0].title, "Book1")

    def test_change_status(self):
        self.library.add_book("Book1", "Author1", 2000)
        book_id = max(self.library.books.keys())

        # Test changing status from "в наличии" to "выдана"
        self.library.change_status(book_id, "выдана")
        self.assertEqual(self.library.books[book_id].status, "выдана")

        # Test changing status from "выдана" to "в наличии"
        self.library.change_status(book_id, "в наличии")
        self.assertEqual(self.library.books[book_id].status, "в наличии")

        # Test invalid status change
        self.library.change_status(book_id, "недопустимый статус")
        self.assertNotEqual(self.library.books[book_id].status, "недопустимый статус")

    def test_serialize_and_deserialize_library(self):
        self.library.add_book("Book1", "Author1", 2000)
        self.library.add_book("Book2", "Author2", 2005)

        # Test serialization
        self.library.serialize_library()
        self.assertTrue(os.path.exists("library_data.json"))

        # Test deserialization
        self.library.books = {}
        self.library.deserialize_library()
        self.assertEqual(len(self.library.books), 2)


if __name__ == '__main__':
    unittest.main()
