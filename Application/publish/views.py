from pathlib import Path
from typing import Any
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from markdown import markdown


class HelloWorldView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")


class DocView(TemplateView):
    template_name = 'doc.html'

    def get_context_data(self, **kwargs):
        text = Path('README.md').read_text()
        kwargs['doc'] = markdown(text)
        return super().get_context_data(**kwargs)
