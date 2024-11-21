from library import Book, Library
from serializer import LibrarySerializer

if __name__ == "__main__":
    library = Library()

    # Добавление нескольких книг
    library.add_book( "Python Programming", "John Doe", 2021)
    library.add_book("Data Science Handbook", "Jane Smith", 2020)

    # Сохранение библиотеки в файл
    LibrarySerializer.save_to_file(library.books, "library_data.json")

    # Загрузка библиотеки из файла
    library.books = LibrarySerializer.load_from_file("library_data.json")

    # Поиск книг по заданному термину
    found_books = library.search_book("Python")
    for book in found_books:
        print(f"Found Book: {book.title} by {book.author}")

    # Обновление статуса книг из JSON данных
    json_data = '[{"id": 1, "status": "выдана"}, {"id": 2, "status": "в наличии"}]'
    LibrarySerializer.update_status_from_json(library.books, json_data)

    # Отображение всех книг после обновления статусов
    library.display_books()