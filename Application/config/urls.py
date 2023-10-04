from django.urls import path

from publish.views import DocView, HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('', DocView.as_view())
]
