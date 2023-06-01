chcp 1251
echo off
cls
echo Создание виртуального окружения:
echo python -m venv venv
echo Активация виртуального окружения для Windows:
echo + venv\Scripts\activate.bat
echo Скачать зависимости:
echo pip install -r requirements.txt
echo Запуск скрипта python main.py
cmd /k 

