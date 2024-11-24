import argparse
from library import Library

'''
Терминальные команды для интерфейса CLI:
1.	Добавление книги:
python cli.py --add "Book Title" "Author Name" Year

2.	Удаление книги:
python cli.py --remove Book_ID

3.	Поиск книги:
python cli.py --search "Search Term"

4.	Отображение всех книг:
python cli.py --display

5.	Изменение статуса книги:
python cli.py --change_status Book_ID status

6. Отображение книги по id:
python cli.py --get Book_ID

'''


def main():
    parser = argparse.ArgumentParser(description='Library Management System')
    parser.add_argument('--add', nargs=3, metavar=('title', 'author', 'year'), help='Add a new book to the library')
    parser.add_argument('--remove', type=int, help='Remove a book by ID')
    parser.add_argument('--search', type=str, help='Search for a book by title, author, or year')
    parser.add_argument('--display', action='store_true', help='Display all books in the library')
    parser.add_argument('--change_status', nargs=2, metavar=('book_id', 'new_status'),
                        help='Change the status of a book by ID')
    parser.add_argument('--get', type=int, help='Get a book by its ID')

    args = parser.parse_args()

    library = Library()
    library.deserialize_library()

    if args.add:
        library.add_book(args.add[0], args.add[1], int(args.add[2]))
        library.serialize_library()
    elif args.remove:
        library.remove_book(args.remove)
        library.serialize_library()
    elif args.search:
        found_books = library.search_book(args.search)
        for book in found_books:
            print(book)
    elif args.display:
        library.display_all_books()
    elif args.change_status:
        book_id, new_status = args.change_status
        library.change_status(int(book_id), new_status)
        library.serialize_library()
    elif args.get:
        book = library.get_book(args.get)
        print(book)


if __name__ == "__main__":
    main()
