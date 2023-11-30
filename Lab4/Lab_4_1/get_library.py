# импортируем необходимые модули
from jinja2 import Template
import sqlite3
from library_model import *

# устанавливаем соединение с базой данных (базу данных взять из ЛР 1)
conn = sqlite3.connect("library.db")

# открываем шаблон из файла library_templ.html и читаем информацию
f_template = open("library_templ.html", "r", encoding="utf-8")
html = f_template.read()
f_template.close()

# создаем объект-шаблон
template = Template(html)

# генерируем результат на основе шаблона
result_html = template.render(
    tables=[
        get_publisher(conn),
        get_genre(conn),
        get_author(conn),
        get_book(conn),
        get_reader(conn),
        get_book_author(conn),
        get_book_reader(conn),
    ],
    table_names=["publisher", "genre", "author", "book", "reader", "book_author", "book_reader"],
    len=len,
    zip=zip,
)

# создаем файл для HTML-страницы
f = open('library.html', 'w', encoding='utf-8-sig')

# выводим сгенерированную страницу в файл
f.write(result_html)
f.close()
