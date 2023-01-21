from django.db import models

class Servusers(models.Model):

    name = models.CharField(max_length=10)
    sname = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    spec_id = models.ForeignKey('Specs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Specs(models.Model):
    spec = models.CharField(max_length=30)

    def __str__(self):
        return self.spec