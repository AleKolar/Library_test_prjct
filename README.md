Проблема с разбором JSON данных из строки serialized_books, а именно по ключу status: Мы это видим при использовании терминальной команды:

python cli.py --display

Output:

[{"ID": 5, "Title": "Python Programming", "Author": "John Doe", "Year": 2021, "Status": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}, {"ID": 6, "Title": "Data Science Handbook", "Author": "Jane Smith", "Year": 2020, "Sta
tus": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}, {"ID": 7, "Title": "Arthur king", "Author": "Mary Ann", "Year": 2000, "Status": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}, {"ID": 8, "Title": "OoooOoooo", "Author": "CooOooo", "Year": 1777, "Status": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}]

Но данные корректны !
Из-за того, что: 
class Book:
    next_id: int = 1  # автоинкрементация начиная с 1 ( Можно сделать по умолчанию )

    def __init__(self, title: str, author: str, year: int, status = "в наличии"):
        self.id: int = Book.next_id
        Book.next_id += 1
        self.title: str = title
        self.author: str = author
        self.year: int = year
        self.status: str = status  # "в наличии"

Во избежании путаницы рекомендуется пользоваться либо Пользовательской панелью cli, либо классической ООП-ой из файла main.py !

