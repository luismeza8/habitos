from django.db import models

from users.models import CustomUser

# Create your models here.
class Habito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100)


class Dia(models.Model):
    habito = models.ForeignKey(Habito, on_delete=models.CASCADE)
    fecha = models.DateField()
