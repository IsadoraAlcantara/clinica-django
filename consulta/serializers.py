from rest_framework import serializers

from .models import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = (
            "id",
            "data_hora_cria_agendamento",
            "tipo_atedimento",
            "agenda_dia_hora_inicio",
            "agenda_dia_hora_final",
            "agenda_status",
            "valor_consulta",
            "hipotese_diagnostica",
            "exame_fisico_pdf",
            "diagnostico_definido",
            "ficha_anamnese_pdf",
            "descricao_consulta",
            "valor_total_exame_consulta",
        )
