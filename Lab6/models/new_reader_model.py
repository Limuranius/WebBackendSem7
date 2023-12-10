import sqlite3


def create_reader(conn: sqlite3.Connection, reader_name: str):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO reader(reader_name)
        VALUES (:reader_name)
    """, {"reader_name": reader_name})
    return cur.lastrowid
