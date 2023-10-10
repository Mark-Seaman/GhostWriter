from django.db import models


class Doc(models.Model):

    path = models.CharField(max_length=200)
