from django.db import models


# Create your models here.
class Vscounter(models.Model):
    user = models.CharField(max_length=255,null=True)
    created = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user