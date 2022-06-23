# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------

class StringVar:
    """ Уровень 1 """

    def __init__(self, string: str):
        self.string = string

    def set(self):
        self.string = input('Введите новое содержимое:\n')
        return self.string

    def get(self):
        print(f'Содержимое строки: {self.string}')


String = StringVar('Test')
String.get()
String.set()
String.get()
