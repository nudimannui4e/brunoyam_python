# -----------------------------
#                             |
#    github.com/nudimannui4e  |
#                             |
# -----------------------------
import json


class Post:
    title = 'Awesome project'
    content = 'something important'
    date_posted = '2022-07-03'
    author = 'Tolstov'

    def __str__(self):
        return self.title


class Model(Post):

    def Save(self):
        """Получить атрибуты класса Post"""
        x = list(filter(lambda x: not x.startswith('_'), dir(Post)))
        results = {}

        for attribute in x:
            results[attribute] = getattr(Post, attribute)

        with open('date_of_class.json', 'w') as out:
            json.dump(results, out, indent=4)
            print(out)
            #for key, val in results.items():
                #out.write('{}:{}\n'.format(key, val))
                #json.dump(val, out)

        return results




b = Model()
print(b.Save())
