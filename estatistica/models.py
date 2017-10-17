from django.db import models


class Populacao(models.Model):
    id_populacao = models.IntegerField(primary_key=True)
    idade = models.IntegerField()
    candidato = models.CharField(max_length=3)

    def __str__(self):
        return "{} - {} - {}".format(self.id_populacao, self.idade, self.candidato)
