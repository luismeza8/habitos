from django.db import models

from users.models import CustomUser

# Create your models here.
class Habito(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=100)
    creacion = models.DateField(auto_now=True)

    def obtener_ultimos_7_dias(self):
        return self.dia_set.all().order_by('-fecha')[:7]

class Dia(models.Model):
    habito = models.ForeignKey(Habito, on_delete=models.CASCADE)
    fecha = models.DateField()
    realizado = models.BooleanField(default=False)
