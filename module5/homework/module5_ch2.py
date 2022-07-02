# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------
import json


class Post:
    title = 'blablabla'
    content = 'content_blabla'
    date_posted = 'time'
    author = 'author'

    def __str__(self):
        return self.title


class Model(Post):

    def Save(self):
        """Получить атрибуты класса Post"""
        x = list(filter(lambda x: not x.startswith('_'), dir(Post)))
        results = {}

        for attribute in x:
            results[attribute] = getattr(Post, attribute)

        return results

        with open('date_of_class.json', 'w') as out:
            for key, val in d2.items():
                out.write('{}:{}\n'.format(key, val))


b = Model()
print(b.Save())
"""
            if attribute[0] != '_':
                with open('date_of_class.json', 'r') as f:
                    date_of_class = json.load(f)
                if attribute not in date_of_class.keys():
                    date_of_class[attribute] = getattr(Post, attribute)
                    with open('date_of_class.json', 'w') as f:
                        json.dump(date_of_class, f)
"""
