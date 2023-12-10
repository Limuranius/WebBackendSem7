from flask import Flask, session
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
from .controllers import index
from .controllers import new_reader
from .controllers import search
from .controllers import book
