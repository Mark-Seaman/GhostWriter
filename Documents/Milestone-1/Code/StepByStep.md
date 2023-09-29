## Milestone 1 - Coding Step-By-Step

New Project

    cd Application
    django-admin startproject config .
    python manage.py startapp publish

config/settings.py

    INSTALLED_APPS = [
        ...
        'publish',
    ]

config/urls.py

    from django.urls import path
    from publish.views import HelloWorldView

    urlpatterns = [
        path('hello/', HelloWorldView.as_view(), name='hello'),
    ]

Run Server

    python manage.py runserver

    browse to http://127.0.0.1:8000/hello

