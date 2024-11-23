Проблема с разбором JSON данных из строки serialized_books, а именно по ключу status: Мы это видим при использовании терминальной команды:

python cli.py --display

Output:

[{"ID": 5, "Title": "Python Programming", "Author": "John Doe", "Year": 2021, "Status": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}, {"ID": 6, "Title": "Data Science Handbook", "Author": "Jane Smith", "Year": 2020, "Sta
tus": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}, {"ID": 7, "Title": "Arthur king", "Author": "Mary Ann", "Year": 2000, "Status": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}, {"ID": 8, "Title": "OoooOoooo", "Author": "CooOooo", "Year": 1777, "Status": "\u0432 \u043d\u0430\u043b\u0438\u0447\u0438\u0438"}]

status в 16-ой кодировки, но данные корректны ! Сторонние модули нельзя ! 


Во избежании путаницы рекомендуется пользоваться либо Пользовательской панелью cli (При условии, что это не сторонний модуль и не является ограничением по условию ТЗ), либо классической ООП-ой из файла main.py !

