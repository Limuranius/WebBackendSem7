import sqlite3
import pandas as pd

con = sqlite3.connect("library.db")
cur = con.cursor()

with open("library.sql", encoding="utf-8") as f:
    cur.executescript(f.read())


def task_1():
    """
    Задание 1
    Вывести книги, которые были взяты в библиотеке в октябре месяце. Указать фамилии читателей, которые их взяли,
    а также дату, когда их взяли. Столбцы назвать Название, Читатель, Дата соответственно. Информацию отсортировать
    сначала по возрастанию даты, потом в алфавитном порядке по фамилиям читателей, и, наконец, по названиям книг
    тоже в алфавитном порядке.
    """

    # strftime("%m", borrow_date) - взять месяц

    query = """
        SELECT book.title as Название, reader.reader_name as Читатель, book_reader.borrow_date as Дата
        FROM book
        JOIN book_reader USING(book_id)
        JOIN reader USING(reader_id)
        WHERE strftime("%m", book_reader.borrow_date) = "10"
        ORDER BY borrow_date ASC, reader_name ASC, title ASC
    """
    df = pd.read_sql(query, con)
    print(df)


def task_2():
    """
Задание 2
Определить статус каждого читателя. Вывести фамилию читателя и его статус. Если хотя бы одна книга была у читателя
"на руках" более 3 недель, в столбец Статус занести "Чёрный список". Если читатель вовсе не брал пока книг в
библиотеке присвоить ему статус "Неактивный читатель". Статус всех остальных читателей - "Добросовестный читатель".
    """
    query = """
        SELECT 
            r1.reader_name AS Читатель
            CASE
                WHEN NOT EXISTS (SELECT * FROM book_reader br1 WHERE r1.reader_id = br1.reader_id) THEN "Неактивный читатель"
                WHEN EXISTS (SELECT * FROM book_reader br2 WHERE r1.reader_id = br2.reader_id AND 
                    ((br2.return_date IS NULL AND JULIANDAY("now") - JULIANDAY(br2.borrow_date) > 21) OR 
                     (br2.return_date IS NOT NULL AND JULIANDAY(br2.return_date) - JULIANDAY(br2.borrow_date) > 21))) 
                     THEN "Чёрный список" 
                ELSE "Добросовестный читатель"
            END AS Статус
        FROM reader r1 
    """
    df = pd.read_sql(query, con)
    print(df)


def task_3():
    """
    Задание 3
    Найти самые популярные жанры (книги, относящиеся к которым чаще всего брали читатели)
    и вывести все книги, которые относятся к этим жанрам.
    """
    print("Жанры по убыванию популярности:")
    query = """
        SELECT genre.genre_name AS Жанр, COUNT(genre.genre_name) AS Взяли
        FROM genre
        JOIN book USING (genre_id)
        JOIN book_reader USING (book_id)
        GROUP BY genre.genre_name
        ORDER BY Взяли DESC
    """
    df = pd.read_sql(query, con)
    print(df)
    print()

    print("Книги топа-3 популярных жанров")
    query = """
        SELECT book.title, genre.genre_name AS Жанр
        FROM book
        JOIN genre USING (genre_id)
        WHERE book.genre_id in (
            SELECT genre.genre_id
            FROM genre
            JOIN book USING (genre_id)
            JOIN book_reader USING (book_id)
            GROUP BY genre.genre_name
            ORDER BY COUNT(genre.genre_name) DESC
            LIMIT 3
        )
    """
    df = pd.read_sql(query, con)
    print(df)


def task_4():
    """
    Задание 4
    Читатель Самарин С.С. возвращает последнюю взятую книгу в библиотеку. Необходимо актуализировать базу данных:
        - занести текущую дату в столбец return_date соответствующей записи таблицы book_reader;
        - увеличить в таблице book на 1 количество доступных книг (available_numbers) для сдаваемой книги.
    Пояснение. В запросах использовать Фамилии И.О. читателя, а не его id.
    """
    reader_name = "Самарин С.С."

    # Получаем id книги, взятой последней
    cur.execute("""
        SELECT book_reader_id, book_id
        FROM book_reader
        JOIN reader USING (reader_id)
        WHERE reader_name = :reader_name AND book_reader.return_date IS NULL
        ORDER BY borrow_date DESC
        LIMIT 1
    """, {"reader_name": reader_name})
    book_reader_id, book_id = cur.fetchone()

    # Заносим дату в столбец return date
    cur.execute("""
        UPDATE book_reader 
        SET return_date = DATE("now")
        WHERE book_reader_id = :book_reader_id
    """, {"book_reader_id": book_reader_id})

    # Увеличить счётчик книги
    cur.execute("""
        UPDATE book
        SET available_numbers = available_numbers + 1
        WHERE book_id = :book_id
    """, {"book_id": book_id})


def task_5():
    """
    Задание 5
    Для тех книг, которые читатели брали больше одного раза, вывести, сколько раз брали каждую книгу,
    а также минимальную разницу в днях между датами, когда читатели ее брали.
    Столбцы назвать Название, Количество, Минимальный_период.
    Информацию отсортировать сначала по возрастанию минимального периода, а затем по названиям книг в алфавитном порядке

    Пояснение. Предположим, что одну и ту же книгу читатели взяли в следующие даты
    2020-10-12, 2020-11-05, 2020-11-15. Минимальный_период вычисляется так:
        - сначала вычисляется разница между следующей и предыдущей датой
          (в нашем случае между первой и второй датой прошло 24 дня, между второй и третьей 10 дней);
        - затем находится минимальное значение (в нашем случае это 10).
    Примечание. Для решения задания № 5 использовать оконные функции.
    """

    query = """
        SELECT book_id, 
            COUNT(*) as Количество,
            JULIANDAY(borrow_date) - JULIANDAY(LAG(borrow_date) OVER (PARTITION BY book_id ORDER BY borrow_date)) as Минимальный_период
        FROM book_reader
        GROUP BY book_id
    """
    df = pd.read_sql(query, con)
    print(df)


# task_1()
# task_2()
# task_3()
# task_4()
task_5()
