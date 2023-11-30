import jinja2

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader("."),
)
template = env.get_template("input.html")

input_data = {
    1: "синий",
    2: "зеленый",
    3: "красный"
}

result = template.render(
    data=input_data,
    name="Some_name",
    select_key=3
)

with open("output.html", "w", encoding="utf-8") as f:
    f.write(result)
