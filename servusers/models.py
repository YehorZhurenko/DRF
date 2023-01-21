from django.db import models

class Servusers(models.Model):

    name = models.CharField(max_length=10)
    sname = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    spec = models.CharField(max_length=30)

    def __str__(self):
        return self.name
