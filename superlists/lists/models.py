from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
    text = models.TextField(default = '')
    pass
