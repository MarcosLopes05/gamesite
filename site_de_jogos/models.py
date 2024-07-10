from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    lancamento = models.DateField()
    plataforma = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
