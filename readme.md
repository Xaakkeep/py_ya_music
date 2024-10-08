# Скрипт для скачивания с Яндекс Музыки

Скрипт качает с сервиса [Yandex Music](https://music.yandex.ru/) из плейлиста "Мне нравиться" все песни.

Скрипт написан на библиотеке [yandex-music 2.2.0](https://pypi.org/project/yandex-music/) Автор [Ilya (Marshal)](ilya@marshal.dev)

Получение токена от автора [NicWeiss](https://github.com/NicWeiss)

[**Документация библиотеки**](https://yandex-music.readthedocs.io/en/latest/index.html)

## Настройка

Для правильной работы скрипта должен быть установлен Chrome без него не заработает!

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

Дальше запустить скрипт и проходим авторизацию(авторизация нужна для получения токена, проходит один раз)

```cmd
python main.py
```

Для Windows можно запустить скрипт установки для PowerShell setup.ps1, а потом run.ps1 для запуска самого скрипта
