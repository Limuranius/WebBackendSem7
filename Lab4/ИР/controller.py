from jinja2 import Template
import sqlite3
import model

READER_ID = 2
SELECTED_MONTH = 10

MONTHS = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь",
}

with sqlite3.connect("library.db") as conn:
    df_book_reader = model.get_readers_by_month(conn, READER_ID, SELECTED_MONTH)
    df_reader = model.get_reader(conn)
with open("template.html", "r", encoding="utf-8") as f_template:
    html = f_template.read()
template = Template(html)
result_html = template.render(
    reader_id=READER_ID,
    readers=df_reader,
    book_readers=df_book_reader,
    months=MONTHS,
    selected_month=SELECTED_MONTH,
    len=len,
    zip=zip
)
with open('output.html', 'w', encoding='utf-8-sig') as f:
    f.write(result_html)
