from typing import List

"""
Инициализация класса Книга
"""
class Book:
    next_id: int = 1  # автоинкрементация начиная с 1

    def __init__(self, title: str, author: str, year: int):
        self.id: int = Book.next_id
        Book.next_id += 1
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = "в наличии"


"""
Инициализация класса Библиотека, где Библиотека - объект словарь(хранилище) с ключами: атрибуты класса Книга
"""
class Library:
    def __init__(self):
        self.books: dict[int, Book] = {}

    """
    Добавляем книгу
    """
    def add_book(self, title: str, author: str, year: int) -> None:
        book: Book = Book(title, author, year)
        self.books[book.id] = book

    """
    Удаляем книгу
    Я рискну не писать блок try except, так как при работе со словарем, в худшем случае, просто будет выведено "Book not found"
    """
    def remove_book(self, book_id: int) -> None:
        if book_id in self.books:
            del self.books[book_id]
        else:
            print("Book not found")

    """
    Ищем книгу по ключам
    """
    def search_book(self, search_term: str) -> List[Book]:
        found_books: List[Book] = []
        book_found: bool = False
        for book_id, book in self.books.items():
            if search_term in [book.title, book.author, str(book.year)]:
                found_books.append(book)
                book_found = True
        if book_found:
            print("Books found!")
            for book in found_books:
                print(f"Found Book: {book.title} by {book.author}")
        else:
            print("No books found.")
        return found_books

    """
    Отображение нашей библиотеки со всеми книгами
    """

    def display_books(self) -> None:
        for book_id, book in self.books.items():
            print(
                f"ID: {book_id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
    """
    Меняем status в логике , либо книга "в наличии", либо её нет, так как она - "выдана"
    """
    def change_status(self, book_id: int, new_status: str) -> None:
        if book_id in self.books:
            current_status: str = self.books[book_id].status
            if current_status == "в наличии" and new_status == "выдана":
                self.books[book_id].status = new_status
            elif current_status == "выдана" and new_status == "в наличии":
                self.books[book_id].status = new_status
            else:
                print("Invalid status change. The book is currently " + current_status)
        else:
            print("Book not found")
