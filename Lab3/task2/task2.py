import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("."),
)
template = env.get_template("input.html")

books = [
    {"title": "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title": "Белая гвардия",
     "author": "Булгаков М.А.",
     "price": 600.00},
    {"title": "Война и мир",
     "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title": "Анна Каренина",
     "author": "Толстой Л.Н.",
     "price": 450.10},
    {"title": "Игрок",
     "author": "Достоевский Ф.М.",
     "price": 234.55},

    {"title": "Мастер и Маргарита",
     "author": "Булгаков М.А.",
     "price": 581.50},
    {"title": "Белая гвардия",
     "author": "Булгаков М.А.",
     "price": 600.00},
    {"title": "Война и мир",
     "author": "Толстой Л.Н.",
     "price": 899.99},
    {"title": "Анна Каренина",
     "author": "Толстой Л.Н.",
     "price": 450.10},
    {"title": "Игрок",
     "author": "Достоевский Ф.М.",
     "price": 234.55}
]

result = template.render(
    data=books,
    n=10
)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(result)
