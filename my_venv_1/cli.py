import argparse
from library import Library
from serializer import LibrarySerializer

'''
Терминальные команды для интерфейса CLI:
1.	Добавление книги:
python cli.py add

2.	Удаление книги:
python cli.py remove

3.	Поиск книги:
python cli.py search

4.	Отображение всех книг:
python cli.py display

5.	Изменение статуса книги:
python cli.py change_status

'''
def main():
    parser = argparse.ArgumentParser(description='Library Management System')
    parser.add_argument('--add', nargs=3, metavar=('title', 'author', 'year'), help='Add a new book to the library')
    parser.add_argument('--remove', type=int, help='Remove a book by ID')
    parser.add_argument('--search', type=str, help='Search for a book by title, author, or year')
    parser.add_argument('--display', action='store_true', help='Display all books in the library')

    args = parser.parse_args()

    library = Library()
    library_data_file = 'C:/Users/User/PycharmProjects/Test_Project_8/my_venv_1/library_data.json'

    library_data = LibrarySerializer.load_from_file(library_data_file)

    for book in library_data.values():
        library.add_book(book.title, book.author, book.year)

    if args.add:
        title, author, year = args.add
        library.add_book(title, author, int(year))
        LibrarySerializer.save_to_file(library.books, library_data_file)
    elif args.remove:
        library.remove_book(args.remove)
        LibrarySerializer.save_to_file(library.books, library_data_file)
    elif args.search:
        library.search_book(args.search)
    elif args.display:
        library.display_books()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()