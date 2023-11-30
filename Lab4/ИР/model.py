import pandas as pd


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_readers_by_month(conn, reader_id: int, month: int):
    """
    Вывести книги, которые были взяты в библиотеке в октябре месяце.
    Указать фамилии читателей, которые их взяли а также дату, когда их взяли.
    Столбцы назвать Название, Читатель, Дата соответственно.
    Информацию отсортировать сначала по возрастанию даты,
    потом в алфавитном порядке по фамилиям читателей, и,
    наконец, по названиям книг тоже в алфавитном порядке.

    Если reader_id == -1, то вывести все книги
    """
    query = """
        SELECT book.title as Название, reader.reader_name as Читатель, book_reader.borrow_date as Дата
        FROM book
        JOIN book_reader USING(book_id)
        JOIN reader USING(reader_id)
        WHERE 
            strftime("%m", book_reader.borrow_date) = :month
            AND
            reader_id = :reader_id
        ORDER BY borrow_date ASC, reader_name ASC, title ASC
    """
    df = pd.read_sql(query, conn, params={
        "reader_id": reader_id,
        "month": str(month)
    })
    return df
