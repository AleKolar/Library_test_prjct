import json

from library import Book

file_name = 'C:/Users/User/PycharmProjects/Test_Project_8/my_venv_1/library_data.json'

class LibrarySerializer:
    @staticmethod
    def to_json(books):
        return json.dumps([book.__dict__ for book in books.values()])

    @staticmethod
    def from_json(json_data):
        book_data_list = json.loads(json_data)
        books = {}

        for book_data in book_data_list:
            if all(key in book_data for key in ['id', 'title', 'author', 'year']):
                book_id = book_data['id']
                books[book_id] = Book(book_id, book_data['title'], book_data['author'], book_data['year'])
            else:
                print(f"Недостаточно данных для создания книги: {book_data}")

        return books

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
        book_updates = json.loads(json_data)

        for update in book_updates:
            if 'id' in update and 'status' in update:
                book_id = update['id']
                new_status = update['status']
                if book_id in books:
                    books[book_id].status = new_status
                    print(f"Статус книги с ID {book_id} успешно обновлен")
                else:
                    print(f"Книга с ID {book_id} не найдена")
            else:
                print("Некорректные данные обновления статуса книги")

        LibrarySerializer.save_to_file(books, file_name)

    @staticmethod
    def serialize_display_books(books):
        serialized_books = []
        for book_id, book in books.items():
            serialized_books.append({
                "ID": book_id,
                "Title": book.title,
                "Author": book.author,
                "Year": book.year,
                "Status": book.status
            })
        return json.dumps(serialized_books)



