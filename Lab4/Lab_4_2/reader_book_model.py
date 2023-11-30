import pandas as pd


def get_reader(conn):
    return pd.read_sql("SELECT * FROM reader", conn)


def get_book_reader(conn, reader_id: int):
    return pd.read_sql("""
        SELECT book_reader.* 
        FROM book
        JOIN book_reader
        USING (book_id)
        WHERE reader_id = ?
    """, conn, params=(reader_id, ))
