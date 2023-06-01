# Скрипт для скачивания с Яндекс Музыки

Скрипт качает с сервиса [Yandex Music](https://music.yandex.ru/) из плейлиста "Мне нравиться" все песни.

Скрипт написан на библиотеке [yandex-music 2.1.1](https://pypi.org/project/yandex-music/) Автор [Ilya (Marshal)](ilya@marshal.dev)

[**Документация библиотеки**](https://yandex-music.readthedocs.io/en/latest/index.html)

**Настройка**

Скачать [скрипт](https://github.com/Xaakkeep/py_ya_music/archive/refs/heads/master.zip) и распаковать его в нужную вам папку

Настроить виртуальное окружение python и активировать

Создание виртуального окружения:

```cmd
python -m venv venv
```

Активация виртуального окружения для Windows:

+ venv\Scripts\activate.bat - для Windows
+ source venv/bin/activate - для Linux и MacOS

Скачать зависимости:

```cmd
pip install -r requirements.txt
```

Прежде чем запускать нужно получить Токен - [Как получить токен](https://yandex-music.readthedocs.io/en/latest/token.html)

После получения токена нужно создать файл settings.ini и прописать в нем токен:

```ini
[Yandex]
TOKEN = Ваш токен
```

Дальше запустить скрипт

```cmd
python main.py
```
