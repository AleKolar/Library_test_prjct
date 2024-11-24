import json
from typing import List

file_path = "C:/Users/User/PycharmProjects/Test_Project_8/my_venv_1/library_data.json"

"""
Инициализация класса Книга
"""


class Book:
    def __init__(self, id: int, title: str, author: str, year: int, status="в наличии"):
        self.id: int = id
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status

    # def serialize(self):
    #     return {
    #         "id": self.id,
    #         "title": self.title,
    #         "author": self.author,
    #         "year": self.year,
    #         "status": self.status
    #     }

    def __str__(self):
        return f"Book: {self.title} by {self.author} ({self.year})"


"""
Инициализация класса Библиотека, где Библиотека - объект словарь(хранилище) с ключами: атрибуты класса Книга
"""


class Library:
    def __init__(self):
        self.books: dict[int, Book] = {}

    def __str__(self):
        return "\n".join([f"Book {book_id}: {book}" for book_id, book in self.books.items()])

    def load_library_data(self):
        try:
            with open('library_data.json', 'r') as file:
                self.books = json.load(file)
        except FileNotFoundError:
            print("Library data file not found. Starting with an empty library.")
            self.books = []

    def save_library_data(self):
        data = {book_id: book.serialize() for book_id, book in self.books.items()}
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    '''
    Преобразуем объекты Python в данные JSON 
    '''

    def serialize_library(self) -> None:
        data = {book_id: book.__dict__ for book_id, book in self.books.items()}
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)

    '''
    Преобразуем данные JSON в объекты Python
    '''

    def deserialize_library(self) -> None:
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                self.books = {int(book_id): Book(**book_data) for book_id, book_data in data.items()}
        except FileNotFoundError:
            print("Library not found. Empty library.")

    '''
    Получаем книгу по её id
    '''

    def get_book(self, book_id):  # Отображаем книгу по id (Для визуализации)
        if book_id in self.books:
            book = self.books[book_id]
            print(f"Book ID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Year: {book.year}")
            print(f"Status: {book.status}")
            return book
        else:
            return None

    """
    Добавляем книгу
    """

    def add_book(self, title, author, year, status="в наличии"):
        book_id = max(self.books.keys(), default=0) + 1
        self.books[book_id] = Book(book_id, title, author, year, status)

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

    def search_book(self, search_term: str | int) -> List[Book]:
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

    def display_all_books(self) -> None:
        if self.books:
            for book_id, book in self.books.items():
                print(
                    f"ID: {book_id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
        else:
            print("No books in the library")

    """
    Меняем status в логике , либо книга "в наличии", либо её нет, так как она - "выдана"
    """

    def change_status(self, book_id: int, new_status: str) -> None:
        if book_id in self.books:
            current_status: str = self.books.get(book_id).status
            if current_status == "в наличии" and new_status == "выдана":
                self.books.get(book_id).status = new_status
                print("Status changed successfully")
            elif current_status == "выдана" and new_status == "в наличии":
                self.books.get(book_id).status = new_status
                print("Status changed successfully")
            else:
                print("Invalid status change. The book is currently " + current_status)
        else:
            print("Book not found")
