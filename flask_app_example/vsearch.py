# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------


def search4vowels(phrase: str) -> set:
    """ Возвращает множество букв, найденых в фразе """
    return set('aeiou').intersection(set(phrase))

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """ Возвращает множество букв из letters, найденых в phrase"""
    return set(letters).intersection(set(phrase))
