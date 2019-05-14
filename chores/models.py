from django.db import models
from django.contrib.auth.models import User
import datetime

class Type(models.Model):
    type_text = models.CharField(max_length = 100)

    def __str__(self):
        return self.type_text

class Chore(models.Model):
    chore_text = models.CharField(max_length=200)
    chore_points = models.IntegerField(default=5)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.chore_text

class Chore_done(models.Model):
    chore = models.ManyToManyField(Chore)
    date_done = models.DateTimeField(default=datetime.datetime.now)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.date_done

