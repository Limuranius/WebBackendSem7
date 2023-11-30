from .complex_number import ComplexFormat

operations = {
    "Действительная часть": lambda z: z.real,
    "Мнимая часть": lambda z: z.im,
    "Модуль": lambda z: z.modulus(),
    "Все формы": lambda z: ", ".join([z.to_format(form) for form in ComplexFormat]),
}

complex_input_fields = {
    ComplexFormat.EULER: [("r", "Радиус"), ("phi", "Угол")],
    ComplexFormat.POLAR: [("r", "Радиус"), ("phi", "Угол")],
    ComplexFormat.REGULAR: [("real", "Действительная часть"), ("im", "Мнимая часть")],
}