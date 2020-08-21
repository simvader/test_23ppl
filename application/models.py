from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(
        max_length=10,
        unique=True
    )
    description = models.TextField(
        max_length=255
    )


class Vaccination(models.Model):
    rut = models.CharField(max_length=15)
    dose = models.FloatField()
    date = models.DateTimeField()
    drug = models.ForeignKey(
        'Drug',
        on_delete=models.PROTECT,
        related_name="vaccination",
    )
