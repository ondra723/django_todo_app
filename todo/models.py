from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(null=True, blank=True)
    # create_date = models.DateTimeField(auto_now_add=True)
    # deadline_date = models.DateTimeField(auto_now_add=False, blank=True, null=True)


    def __str__(self):
        return self.text