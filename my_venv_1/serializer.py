import json

from my_venv_1.library import Book


class LibrarySerializer:
    @staticmethod
    def to_json(books):
        return json.dumps([book.__dict__ for book in books.values()])

    @staticmethod
    def from_json(json_data):
        return {book_data['id']: Book(book_data['title'], book_data['author'], book_data['year']) for book_data in json.loads(json_data)}

    @staticmethod
    def save_to_file(books, file_name):
        with open(file_name, 'w') as file:
            json.dump(LibrarySerializer.to_json(books), file)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as file:
            return LibrarySerializer.from_json(json.load(file))

    @staticmethod
    def update_status_from_json(books, json_data):
        for book_data in json.loads(json_data):
            if book_data['id'] in books:
                books[book_data['id']].status = book_data['status']