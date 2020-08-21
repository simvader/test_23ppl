from django.db import models

class Drug(models.Model):
    name = models.CharField(max_lenght=200)
    code = models.CharField(
        max_lenght=10,
        unique=True
    )
    description = models.TextField()


class Vaccination(models.Model):
    rut = models.IntegerField()
    dose = models.FloatField()
    date = models.DateTimeField()
