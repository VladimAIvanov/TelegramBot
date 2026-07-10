#!/bin/bash

# 1. Создать и активировать виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 2. Установить зависимости
pip install -r requirements.txt

# 3. (Опционально) Создать или обновить .env с токеном
echo "BOT_TOKEN=ваш_токен_здесь" > .env

# 4. Запустить приложение
python main.py

# 5. Деактивировать окружение (опционально)
deactivate