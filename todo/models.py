
from django.db.models import Model, CharField, BooleanField, DateTimeField
from django.utils import timezone


class Todo(Model):
    text = CharField(max_length=40)
    complete = BooleanField(default=False)
    date = DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text