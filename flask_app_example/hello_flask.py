# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

from flask import Flask, render_template
from vsearch import search4letters
"""
__name__ - устанавливает имя активного модуля
Flask нужно знать его значение, когда создается
новый объект Flask (app)
"""
app = Flask(__name__)

"""
Это декоратор функции route - изменяет поведение
текущей функции, без (!) изменения её кода 
"""


@app.route('/')
def hello() -> str:
    return 'Hello from Flask!'


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    return str(search4letters('Life, the universe, and everything!', 'eiru,!'))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


app.run(debug=True)
