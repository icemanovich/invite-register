# invite-register


## Задача

Написать сервис регистрации по инвайту.
Основная логика работы:
на главной выводить 2 разные страницы: одна - для авторизованных (со сылкой “Выйти”), 
другая - для остальных (форма ввода логина и пароля)
при создании инвайта (в админке) уходит письмо на емейл счастливчика
в письме ссылка, при переходе по которой, создается юзер и авторизуется пользователь
после создания пользователю уходит емейл с логином и паролем

Дополнительные требования:
инвайт не может быть использован повторно
инвайт после использования должен быть привязан к пользователю
наличие тестов

в качестве базы - sqlite
в качестве емейл бэкенда - консоль


## Требования
1. Python версии 3.4
2. Установленный пакетный менеджер pip
---

## Развёртывание проекта

1. Установить зависимости
```
pip install -r requirements.txt
```

2. Создать файл .env и внести в него нужные параметры
```
cp .env_example .env
nano .env
```

3. Создать пользователей по-умолчанию (Админа)
```
Доступные аккаунты:
admin@example.com / qwe
master@example.com / qwe

python manage.py create_default_users

```

4. Запустить приложение
```
python run.py

либо

./runserver.sh

```
