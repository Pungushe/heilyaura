# Репозиторий heilyaura (Магазин товаров)

Этот репозиторий содержит код для создания интернет-магазина с использованием Django и Tailwind CSS.

Установка (для пользователей операционных систем семейства MacOs/Linux/Windows):

Открыть терминал или консоль и перейти в нужную Вам директорию. Прописать команду `git clone git@github.com:Pungushe/heilyaura.git`

Если Вы используете https, то: `https://github.com/Pungushe/heilyaura.git`

## Установка webhook для Stripe

'''commandline
     .\stripe login  
'''

## Локальное прослушивание  вебхуков Stripe

'''commandline
     stripe listen --forward-to localhost:4242/webhook
'''

## Настройки локального прослушивателя вебхуков Stripe

'''commandline
     stripe listen --forward-to localhost:8000/payment/webhook
'''

## Создаем суперпользователя Docker
'''commandline
     docker-compose run web py manage.py createsuperuser
'''
