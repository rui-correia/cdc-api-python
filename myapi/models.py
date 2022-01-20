from django.db import models

# Create your models here.
class Autor(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Categoria(models.Model):
    nome = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.nome