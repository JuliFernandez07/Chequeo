from django.db import models

# Create your models here.
class familiares(models.Model):
    nombre = models.CharField(max_length=30)
    nacimiento = models.DateField()
    parentesco = models.CharField(max_length= 15)
