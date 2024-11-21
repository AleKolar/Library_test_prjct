'''
ТЕСТЫ, у меня на уровне:

result = add(3, 4)
self.assertEqual(result, 7)

не хотел копипастить, подумал есть возможность изучить/закрепить материал, но в итоге все по книжке (документации) и вот так !
'''

import unittest
from library import Book, Library

class TestLibraryFunctions(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", 2022)
        self.assertEqual(len(self.library.books), 1)

    def test_remove_book(self):
        self.library.add_book("Test Book", "Test Author", 2022)
        book_id = list(self.library.books.keys())[0]
        self.library.remove_book(book_id)
        self.assertNotIn(book_id, self.library.books)

    def test_search_book(self):
        self.library.add_book("Test Book", "Test Author", 2022)
        found_books = self.library.search_book("Test Book")
        self.assertEqual(len(found_books), 1)

    def test_change_status(self):
        self.library.add_book("Test Book", "Test Author", 2022)
        book_id = list(self.library.books.keys())[0]
        self.library.change_status(book_id, "выдана")
        self.assertEqual(self.library.books[book_id].status, "выдана")

if __name__ == '__main__':
    unittest.main()