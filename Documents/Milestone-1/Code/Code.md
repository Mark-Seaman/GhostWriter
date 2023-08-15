# Milestone 1 - Code 

Create a simple app that runs on the server.

It does not do anything interesting other that show a hard-coded web page.


## What I did 

Install development tools

    Setup Python 3.11

    Install Django (pip install django)

    Create the Git Repo for Project and Documents

    Install Visual Studio Code and setup Github connection

Create a Django app 

    mkdir GhostWriterApp
    
    cd GhostWriterApp

    python -m django startproject config .

    python manage.py startapp publish

config/settings.py

    ALLOWED_HOSTS = ['*']

    INSTALLED_APPS = [
        ...
        'django.contrib.staticfiles',
        'publish',
    ]

publish/views.py

    from django.http import HttpResponse
    from django.views import View

    class HelloWorldView(View):
        def get(self, request):
            return HttpResponse("Hello, World!")

config/urls.py

    from django.urls import path
    from publish.views import HelloWorldView

    urlpatterns = [
        path('hello/', HelloWorldView.as_view(), name='hello'),
    ]

Run Server

    python manage.py runserver


## What I will do

Setup Visual Studio to run the code in the debugger.

Build a view with the defined URL, View, Template design pattern.

Display markdown text from a document files that read.


## Concerns and Challenges


