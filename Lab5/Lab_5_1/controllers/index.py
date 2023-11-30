from app import app
from flask import render_template, request
import constants


@app.route('/', methods=['GET'])
def index():
    form_sent = len(request.values) != 0
    name = request.values.get('username', default="")
    gender = request.values.get('gender', default="")
    program_id = request.values.get('program', default=0)
    subject_id = request.values.getlist('subject[]')
    # формируем список из выбранных пользователем дисциплин
    subjects_select = [constants.subjects[int(i)] for i in subject_id]

    html = render_template(
        'index.html',
        program_list=constants.programs,
        subject_list=constants.subjects,
        len=len,
        name=name,
        gender=gender,
        program=constants.programs[int(program_id)],
        subjects_select=subjects_select,
        form_sent=form_sent,
    )
    return html
