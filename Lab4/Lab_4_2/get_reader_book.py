from jinja2 import Template
import sqlite3
from reader_book_model import get_reader, get_book_reader

READER_ID = 3
with sqlite3.connect("library.db") as conn:
    df_book_reader = get_book_reader(conn, READER_ID)
    df_reader = get_reader(conn)
f_template = open("reader_book_templ.html", "r", encoding="utf-8")
html = f_template.read()
f_template.close()
template = Template(html)
result_html = template.render(
    reader_id=READER_ID,
    combo_box=df_reader,
    book_reader=df_book_reader,
    len=len,
    zip=zip
)
with open('reader_book.html', 'w', encoding='utf-8-sig') as f:
    f.write(result_html)
