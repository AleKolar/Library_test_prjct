class Book:
    next_id = 1  # автоинкреминтация начиная с 1

    def __init__(self, title, author, year):
        self.id = Book.next_id
        Book.next_id += 1
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"


class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, year):
        book = Book(title, author, year)
        self.books[book.id] = book

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
        else:
            print("Book not found")

    def search_book(self, search_term):
        found_books = []
        for book_id, book in self.books.items():
            if search_term in [book.title, book.author, str(book.year)]:
                found_books.append(book)
        return found_books

    def display_books(self):
        for book_id, book in self.books.items():
            print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    def change_status(self, book_id, new_status):
        if book_id in self.books:
            current_status = self.books[book_id].status
            if current_status == "в наличии" and new_status == "выдана":
                self.books[book_id].status = new_status
            elif current_status == "выдана" and new_status == "в наличии":
                self.books[book_id].status = new_status
            else:
                print("Invalid status change. The book is currently " + current_status)
        else:
            print("Book not found")


