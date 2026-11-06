from django.db import models


class Consulta(models.Model):
    data_hora_cria_agendamento = models.DateTimeField()
    tipo_atedimento = models.CharField(max_length=30)
    agenda_dia_hora_inicio = models.DateTimeField()
    agenda_dia_hora_final = models.DateTimeField(null=True, blank=True)
    agenda_status = models.CharField(max_length=30, null=True, blank=True)
    valor_consulta = models.DecimalField(max_digits=10, decimal_places=2)

    hipotese_diagnostica = models.CharField(max_length=500, null=True, blank=True)
    exame_fisico_pdf = models.FileField(
        upload_to="exame_fisico/", blank=True, null=True
    )
    diagnostico_definido = models.CharField(max_length=100, null=True, blank=True)
    ficha_anamnese_pdf = models.FileField(
        upload_to="ficha_anamnese/", blank=True, null=True
    )
    descricao_consulta = models.CharField(max_length=500, null=True, blank=True)
    valor_total_exame_consulta = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )  # FAZER CALCULO COM O VALOR DOS EXAMES

    # especialidade
    # sala
    # plano_saude
    # paciente
    # profissional
    # tratamento

    def __str__(self):
        return f"{self.data_hora_cria_agendamento} - R$ {self.valor_consulta} - {self.tipo_atedimento} - {self.agenda_dia_hora_inicio} - {self.agenda_dia_hora_final} - {self.agenda_status} - {self.hipotese_diagnostica} - {self.exame_fisico_pdf} - {self.diagnostico_definido} - {self.ficha_anamnese_pdf} - {self.descricao_consulta} - {self.valor_total_exame_consulta}"
