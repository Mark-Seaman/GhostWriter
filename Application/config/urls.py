from django.urls import path
from publish.views import HelloWorldView

urlpatterns = [
    path('hello/', HelloWorldView.as_view(), name='hello'),
]
