from library import Book, Library
from serializer import LibrarySerializer

if __name__ == "__main__":
    library = Library()

    # Добавление нескольких книг
    library.add_book( "Python Programming", "John Doe", 2021)
    library.add_book("Data Science Handbook", "Jane Smith", 2020)
    library.add_book("Arthur king", "Mary Ann", 2000)

    # Сохранение библиотеки в файл
    LibrarySerializer.save_to_file(library.books, "library_data.json")

    # Загрузка библиотеки из файла
    library.books = LibrarySerializer.load_from_file("library_data.json")

    # Поиск книг по заданным критериям из ТЗ
    found_books = library.search_book("Python Programming")

    if found_books:
        for book in found_books:
            print(f"Found Book: {book.title} by {book.author}")
    else:
        print("No books found.")

    no_found_books = library.search_book("No Python Programming")

    if no_found_books:
        for book in no_found_books:
            print(f"Found Book: {book.title} by {book.author}")
    else:
        print("No books found.")


    # Обновление статуса книг из JSON данных
    json_data = '[{"id": 1, "status": "выдана"}, {"id": 2, "status": "выдана"}]'
    LibrarySerializer.update_status_from_json(library.books, json_data)

    # Отображение всех книг после обновления статусов
    library.display_books()

    book_id = 1  # Example book ID
    book_1 = library.get_book(book_id)
    print("Вы это искали:", book_1)

    # Вывод информации о книгах до обновления статуса
    print("Books before update:")
    for book_id, book in library.books.items():
        print(f"ID: {book_id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

    # Вызов метода для обновления статуса
    LibrarySerializer.update_status_from_json(library.books, json_data)

    # Вывод информации о книгах после обновления статуса
    print("Books after update:")
    for book_id, library.books in library.books.items():
        print(f"ID: {book_id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")

