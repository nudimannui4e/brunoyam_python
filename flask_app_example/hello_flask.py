# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

from flask import Flask, render_template, request
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

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)
