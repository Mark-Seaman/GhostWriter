from pathlib import Path
from django.test import TestCase
from markdown import markdown


class DocPagesTest(TestCase):

    def test_readme1(self):
        path = Path('README.md')
        self.assertTrue(path.exists())
        self.assertEqual(len(path.read_text()), 2832)

    def test_hello_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_bad_page_view(self):
        response = self.client.get('/x')
        self.assertEqual(response.status_code, 404)
