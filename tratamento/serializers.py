from rest_framework import serializers

from .models import Tratamento


class TratamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tratamento
        fields = (
            "id",
            "status_tratamento",
            "data_inicio_tratamento",
            "descricao_tratamento",
            "data_fim_tratamento",
        )
