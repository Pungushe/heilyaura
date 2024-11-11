# Репозиторий django_shop (Магазин товаров)

Этот репозиторий содержит код для создания интернет-магазина с использованием Django и Tailwind CSS.

Установка (для пользователей операционных систем семейства MacOs/Linux/Windows):

Открыть терминал или консоль и перейти в нужную Вам директорию. Прописать команду `git clone git@github.com:Pungushe/django_shop.git`

Если Вы используете https, то: `https://github.com/Pungushe/django_shop.git`

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

## Установка контейнера Docker

'''commandline
     
     
     docker-compose up --build
'''
