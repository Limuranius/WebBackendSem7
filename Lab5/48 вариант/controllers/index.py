from ..app import app
from flask import render_template, request
from .. import constants
from ..complex_number import ComplexFormat, Complex


@app.route('/', methods=['GET'])
def index():
    show_results = request.values.get("button") == "Отправить"

    real = request.values.get('real', type=int)
    im = request.values.get('im', type=int)

    r = request.values.get("r", type=int)
    phi = request.values.get("phi", type=int)

    if real and im:
        z = Complex(real, im)
        z_form_data = [real, im]
    elif r and phi:
        z = Complex.from_polar(r, phi)
        z_form_data = [r, phi]
    else:
        z = Complex(0, 0)
        z_form_data = [0, 0]

    selected_operations = request.values.getlist("operations")
    selected_format = ComplexFormat(request.values.get('form', default=ComplexFormat.POLAR.value))

    html = render_template(
        'index.html',
        z_form_data=z_form_data,
        form_sent=show_results,
        z=z,
        selected_operations=selected_operations,
        selected_format=selected_format,

        len=len,
        ComplexFormat=ComplexFormat,
        operations=constants.operations,
        complex_input_fields=constants.complex_input_fields
    )
    return html
