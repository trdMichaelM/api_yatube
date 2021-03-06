### Описание проекта:
Учебный проект, предназначенный для отработки навыков и применение теории при разработки
API веб приложений, базируемых на фреймворке Django и модуле Django Rest Framework.
Для обеспечения контороля прав доступа в проекте используется модуль Djoser.

### Установка и запуск проекта:

Клонировать репозиторий и перейти в него в командной строке (используем ssh):

```
git clone git@github.com:trdMichaelM/api_yatube.git
```

```
cd api_yatube
```

Файл .env.example переименовываем в .env и прописываем в нем SECRET_KEY

```
mv .env.example .env
nano .env
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/bin/activate (for Linux)
```

Обновить pip до последней версии:
```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Дополнительно установить модули Djoser и Simple JWT и dotenv:

```
pip install djoser djangorestframework_simplejwt python-dotenv
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры использования API:


```
GET http://127.0.0.1:8000/api/v1/posts/
POST http://127.0.0.1:8000/api/v1/posts/
GET http://127.0.0.1:8000/api/v1/posts/{id}/
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
POST http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
GET http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
GET http://127.0.0.1:8000/api/v1/groups/
GET http://127.0.0.1:8000/api/v1/follow/
POST http://127.0.0.1:8000/api/v1/follow/
```

Более дитальное описание и примеры работы API проекта представлены в 
документации: http://127.0.0.1:8000/api/v1/follow/ в формате ReDoc.

### Используется:

```
Python 3.9 Django 2.2 Djoser
```
