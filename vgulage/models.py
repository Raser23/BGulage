from django.db import models


class User(models.Model):

    name = models.CharField(max_length=100)
    age = models.IntegerField(default=25)
    sex = models.CharField(max_length=20, default='male')
    pswd = models.CharField(max_length=100)

    def __str__(self):
        return self.name