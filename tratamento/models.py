from django.db import models


class Tratamento(models.Model):
    status_tratamento = models.CharField(max_length=20)
    data_inicio_tratamento = models.DateTimeField()
    descricao_tratamento = models.CharField(max_length=500, blank=True, null=True)
    data_fim_tratamento = models.DateTimeField()

    def __str__(self):
        return f"{self.status_tratamento} - {self.data_inicio_tratamento} - {self.descricao_tratamento} - {self.data_fim_tratamento}"
