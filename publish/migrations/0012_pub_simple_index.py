# Generated by Django 4.0.4 on 2023-04-19 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publish', '0011_content_retain_object'),
    ]

    operations = [
        migrations.AddField(
            model_name='pub',
            name='simple_index',
            field=models.BooleanField(default=False),
        ),
    ]
