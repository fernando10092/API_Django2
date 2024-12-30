from django.db import models

class Banco(models.Model):
    nome = models.TextField()
    idade = models.IntegerField()

