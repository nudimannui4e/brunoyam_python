## Создание и установка модулей в Python

- Создание файла описания
- Создание файла дистрибутива
- Установка файла дистрибутива

### Файл описания. Setup.py

```python
from setuptools import setup

setup(
    name='character',
    version='0.0.1',
    description='Первые попытки создать class, и прописать ему методы',
    author='nudimannui4e',
    author_email='nudimannui4e@protonmail.com',
    url='https://nudimannui4e.github.io/',
    py_modules=['character.py']
)
```

### Создание файла дистрибутива

```bash
python3 setup.py sdist

running sdist
running egg_info
creating character.egg-info
writing character.egg-info/PKG-INFO
writing dependency_links to character.egg-info/dependency_links.txt
writing top-level names to character.egg-info/top_level.txt
writing manifest file 'character.egg-info/SOURCES.txt'
error: package directory 'character' does not exist

```