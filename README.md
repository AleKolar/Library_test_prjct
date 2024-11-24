Здравствуйте ! Представляю тестовое задание "Разработка системы управления библиотекой".

Здесь реализованно : 

управление библиотекой книг. Которая позволять добавлять, удалять, искать и отображать книги. Каждая книга должна содержать следующие поля:
 • id (уникальный идентификатор, генерируется автоматически)
 • title (название книги)
 • author (автор книги)
 • year (год издания)
 • status (статус книги: “в наличии”, “выдана”)

В соответствии с требованием реализованно :

 1. Добавление книги: Пользователь вводит title, author и year, после чего книга добавляется в библиотеку с уникальным id и статусом “в наличии”.
 2. Удаление книги: Пользователь вводит idкниги, которую нужно удалить.
 3. Поиск книги: Пользователь может искать книги по title, author или year.
 4. Отображение всех книг: Приложение выводит список всех книг с их id, title, author, year и status.
 5. Изменение статуса книги: Пользователь вводит id книги и новый статус (“в наличии” или “выдана”).

А также: 

 • Реализовать хранение данных в json формате.
 • Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу).
 • Написать функции для каждой операции (добавление, удаление, поиск, отображение, изменение статуса).
 • Не использовать сторонние библиотеки.

 Пояснения к некоторым моментам : 
 Касательно :  Обеспечить корректную обработку ошибок (например, попытка удалить несуществующую книгу). 
 
- Блок try except - пекрасный инструмент , но я взял на себя ответственность его не писать при удалении объекта так как при работе со словарем, в худшем случае, просто будет выведено "Book not found". По моему мнению.
 
Касательно : Не использовать сторонние библиотеки !
- pickle входит в стандартную библиотеку Python, его же нельзя считать сторонней библиотекой !? Тут ладно, обошлось без него. Но я добавил удобную пользовательскую панель cli из из модуля argparse, но это, ведь, стандартная библиотека !
- p.s. Также есть пользовательская панель в файле main.py, где все по Питоновски и прямолинейно !




