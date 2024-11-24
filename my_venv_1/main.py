import json
from library import Book, Library
from serializer import LibrarySerializer
from json.decoder import JSONDecodeError

if __name__ == "__main__":
    library = Library()

    try:
        library.deserialize_library()
    except JSONDecodeError:
        print("Error: JSON file is empty or in incorrect format.")
    except FileNotFoundError:
        print("Error: Library JSON file not found.")

    # Добавляем книгу в library
    library.add_book("Python", "John Doe", 2021)
    library.add_book("Python_2", "Jane Smith", 2020)
    library.add_book("Arthur king", "Mary Ann", 2000)

    # Сериализуем library в JSON file
    library.serialize_library()

    # Изменяем status книги
    book_id_to_change = 1
    new_status = "выдана"  # Change status to "выдана" or "в наличии"
    library.change_status(book_id_to_change, new_status)

    # Удаляем книгу
    book_id_to_delete = 2
    library.remove_book(book_id_to_delete)
    print(f"Book {book_id_to_delete} deleted.")

    # Отображаем книгу с id = 1
    book_id_to_get = 1
    book = library.get_book(book_id_to_get)

    # Ищем книгу по названию
    search_term = "Arthur king"
    found_books = library.search_book(search_term)

    # Сериализуем library снова , после изменения status
    library.serialize_library()

    library.display_all_books()