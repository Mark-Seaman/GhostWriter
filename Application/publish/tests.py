from pathlib import Path
from django.test import TestCase
from markdown import markdown

from .models import Doc


class DocViewTest(TestCase):

    def test_readme(self):
        path = Path('README.md')
        self.assertTrue(path.exists())
        text = path.read_text()
        self.assertEqual(len(text), 733)
        self.assertEqual(text.split('\n')[0],
                         '# Ghost Writer Application Code')

    def test_readme_title(self):
        text = Path('README.md').read_text()
        lines = text.split('\n')
        self.assertEqual(lines[0], '# Ghost Writer Application Code')
        self.assertEqual(len(lines), 28)

    def test_hello_view(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)

    def test_bad_page_view(self):
        response = self.client.get('/x')
        self.assertEqual(response.status_code, 404)

    def test_doc_view(self):
        response = self.client.get('/')
        title1 = 'Document Display View'
        self.assertContains(response, title1)

    def test_markdown_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        text = response.content.decode('utf-8')
        self.assertIn('Ghost Writer Application Code', text)


class DocDataTest(TestCase):

    def test_create_doc(self):
        Doc(path='xxx').save()
        Doc(path='yyy').save()
        docs = Doc.objects.all()
        self.assertEqual(len(docs), 2)

    def test_read_doc(self):
        Doc(path='xxx').save()
        Doc(path='yyy').save()
        doc1 = Doc.objects.get(pk=1)
        doc2 = Doc.objects.get(pk=2)
        self.assertEqual(doc1.path, 'xxx')
        self.assertEqual(doc2.path, 'yyy')

    def test_update_doc(self):
        Doc(path='xxx').save()
        doc = Doc.objects.get(pk=1)
        doc.path = 'yyy'
        doc.save()
        doc = Doc.objects.get(pk=1)
        self.assertEqual(doc.path, 'yyy')

    def test_delete_doc(self):
        Doc.objects.create(path='xxx')
        Doc.objects.all().delete()
        self.assertEqual(len(Doc.objects.all()), 0)


class MarkdownTest(TestCase):

    def test_markdown_paragraph(self):
        text = markdown('xxx')
        self.assertEqual(text, '<p>xxx</p>')

    def test_markdown_heading(self):
        text = markdown('# Heading Title')
        self.assertEqual(text, '<h1>Heading Title</h1>')

    def test_markdown_list(self):
        text = '''
* item 1
* item 2
* item 3
'''
        expected = '''<ul>
<li>item 1</li>
<li>item 2</li>
<li>item 3</li>
</ul>'''
        text = markdown(text)
        self.assertEqual(text, expected)

    def test_links(self):
        text = '[Link Text](url)'
        text = markdown(text)
        self.assertEqual(text, '<p><a href="url">Link Text</a></p>')
