# Создайте некоторую базу данных, используя sqlite3.
# В ней реализуйте 2-3 таблицы, при создании которых используйте различные ограничения и типы данных столбцов.
# После этого наполните таблицу разными данными, используя разные варианты(например, введенные данные вручную,
# данные из какого-то файла и т.д.)
# Также, не забудьте открыть эту базу данных в SQLiteStudio и проверить все свойства. После чего попробуйте написать несколько запросов, использующих связи между таблицами.


# import sqlite3 as sq
#
#
# books = [
#     ('Евгений Онегин', 'А.С.Пушкин', 600),
#     ('Дубровский', 'А.С.Пушкин', 700),
#     ('Азазель', 'Б.Акунин', 1000),
#     ('Федорино горе', 'К.Чуковский', 250),
#     ('Мойдодыр', 'К.Чуковский', 200),
#     ('Бассейн с крокодилами', 'Д.Донцова', 750)
# ]
#
# genres = [
#     ('Евгений Онегин', 'поэма'),
#     ('Дубровский', 'поэма'),
#     ('Азазель', 'детектив'),
#     ('Федорино горе', 'сказка'),
#     ('Мойдодыр', 'сказка'),
#     ('Бассейн с крокодилами', 'детектив')
# ]
#
# with sq.connect('books.db') as con:
#     cur = con.cursor()
#
    # Создание таблицы в бд
    # cur.execute('CREATE TABLE IF NOT EXISTS books('
    #             'book_id INTEGER PRIMARY KEY AUTOINCREMENT,'
    #             'name_book TEXT NOT NULL,'
    #             'author TEXT NOT NULL,'
    #             'price INTEGER CHECK(price >= 0)'
    #             ')')
    #
    # Добавление одного значения/строки
    # cur.execute('INSERT INTO books VALUES(NULL, "Тараканище", "К.Чуковский", 200)')
    #
    # Добавление с помощью цикла
    # for i in range(6):
    #    cur.execute(f'INSERT INTO books VALUES(NULL, "{books[i][0]}", {books[i][1]})')
    #
    # Добавление всех значений
    # cur.executemany('INSERT INTO books VALUES(NULL, ?, ?, ?)', books)

    # Создание таблицы в бд
    # cur.execute('CREATE TABLE IF NOT EXISTS genres('
    #             'genre_id INTEGER PRIMARY KEY AUTOINCREMENT,'
    #             'name_book TEXT NOT NULL,'
    #             'genre TEXT NOT NULL'
    #             ')')
    # Добавление значений в таблицу
    # cur.executemany('INSERT INTO genres VALUES(NULL, ?, ?)', genres)

    # Представление данных из бд в виде sq.Row, что позволяет получать к ним доступ по названиям свойств(столбиков)
    # cur.row_factory = sq.Row
    # cur.execute('''SELECT name_book, price FROM books''')
    # for book in cur:
    #     print(book['name_book'], book[1])

    # cur.execute('SELECT *'
    #             'FROM books ')
    #
    # print(cur.fetchone())
    #
    # cur.execute('SELECT *'
    #             'FROM books ')
    #
    # print(cur.fetchmany(3))
    #
    # cur.execute('SELECT *'
    #             'FROM books '
    #             'WHERE price < 500')
    #
    # print(cur.fetchall())
    #
    # cur.execute('SELECT * '
    #             'FROM books '
    #             'WHERE name_book IN ('
    #             '   SELECT name_book '
    #             '   FROM genres '
    #             '   WHERE genre = "сказка"'
    #             ')')
    #
    # print(cur.fetchall())
    #
    # try:
    #     cur.executescript('BEGIN; '
    #                       'UPDATE books SET price = price - 30; '
    #                       'CREATE TABLE IF NOT EXISTS expensive_books('
    #                       'book_id INTEGER PRIMARY KEY AUTOINCREMENT,'
    #                       'name_book TEXT NOT NULL,'
    #                       'author TEXT NOT NULL,'
    #                       'price INTEGER'
    #                       ');'
    #                       'INSERT INTO expensive_books '
    #                       'SELECT * '
    #                       'FROM books '
    #                       'WHERE price > 500')
    #
    # except sq.Error as e:
    #     print(f'При выполнении операций произошла ошибка: {e}')
    #     if con:
    #         con.rollback()
    # else:
    #     if con:
    #         con.commit()