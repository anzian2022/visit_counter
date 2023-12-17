from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class User(models.Model):
    user = models.TextField(default=None)

    def __str__(self):
        return self.user