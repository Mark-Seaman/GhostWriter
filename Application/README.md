# Ghost Writer Application Code

Code for Project to demonstrate software engineering skills

## Repo Contents

This repo contains three main components

* Ghost Writer - [Project notes](../Documents/README.md)
    * Project notes for example of documentation
    * Deliverables for each milestone
* Ghost Writer - [Application code](../Application/README.md)
    * Application code for software project
    * Provided as an example
* Software Engineering Skills - [Lessons and assignments](../SoftwareEngineering/README.md)
    * 7 Milestones (each with 4 Lessons)
    * Milestone Assignments
    * ChatGPT Prompts

### Git Branches
* m1
* m2
* m3

## Milestone 1 Documents

[Project Milestone 1](../Documents/Milestone-1/Index.md)



## Code Snippets

views.py

    class DocView(TemplateView):
        template_name = 'doc.html'

        def get_context_data(self, **kwargs):
            text = Path('README.md').read_text()
            kwargs['doc'] = markdown(text)
            return super().get_context_data(**kwargs)

urls.py

    path('', DocView.as_view())

tests.py

    from pathlib import Path
    from django.test import TestCase
    from markdown import markdown


    class DocPagesTest(TestCase):

        # def test_readme1(self):
        #     self.assertTrue(Path('README.md').exists())

        # def test_readme2(self):
        #     text = Path('README.md').read_text()
        #     self.assertEqual(len(text), 734)

        # def test_readme3(self):
        #     text = Path('README.md').read_text()
        #     title = text.split('\n')[0]
        #     self.assertEqual(title, '# Ghost Writer Application Code')

        def test_readme(self):
            text = Path('README.md').read_text()
            title = text.split('\n')[0]
            self.assertEqual(len(text), 734)
            self.assertEqual(title, '# Ghost Writer Application Code')

        def test_markdown(self):
            html = markdown('# Rock On')
            self.assertEqual(html, '<h1>Rock On</h1>')

        def test_markdown_file(self):
            text = Path('README.md').read_text()
            html = markdown(text)
            # print(html)
            self.assertEqual(len(html), 932)

        def test_page(self):
            page = '/hello/'
            response = self.client.get(page)
            text = response.content.decode('utf-8')
            # print(text)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(text, 'Hello, World!')

        def test_markdown_page(self):
            page = '/'
            response = self.client.get(page)
            text = response.content.decode('utf-8')
            # print(text)
            self.assertEqual(response.status_code, 200)
            self.assertContains(
                response, '<h1>Ghost Writer Application Code</h1>')
