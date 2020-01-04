import datetime

from django.db import models
from django.utils import timezone


class Nyanpasu(models.Model):
    name = models.CharField(max_length=10, unique=True)
    count = models.BigIntegerField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
