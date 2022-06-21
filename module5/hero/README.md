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
package init file 'character/__init__.py' not found (or not a regular file)
file character/py.py (for module character.py) not found
reading manifest file 'character.egg-info/SOURCES.txt'
writing manifest file 'character.egg-info/SOURCES.txt'
running check
creating character-0.0.1
creating character-0.0.1/character.egg-info
copying files to character-0.0.1...
copying README.txt -> character-0.0.1
copying setup.py -> character-0.0.1
copying character.egg-info/PKG-INFO -> character-0.0.1/character.egg-info
copying character.egg-info/SOURCES.txt -> character-0.0.1/character.egg-info
copying character.egg-info/dependency_links.txt -> character-0.0.1/character.egg-info
copying character.egg-info/top_level.txt -> character-0.0.1/character.egg-info
Writing character-0.0.1/setup.cfg
creating dist
Creating tar archive
removing 'character-0.0.1' (and everything under it)
```

### Установка файла дистрибутива

```bash
python3 -m pip install character-0.0.1.tar.gz
```