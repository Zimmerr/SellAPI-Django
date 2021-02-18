from django.db import models
from django.utils import timezone

# Create your models here.

class Vendedor(models.Model):
  nome = models.CharField(max_length=200)
  data_nasc = models.DateField()
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.nome

vend = Vendedor(nome="Joaozinho", data_nasc="2000-03-03")