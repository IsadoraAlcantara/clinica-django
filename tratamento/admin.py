from django.contrib import admin

from .models import Tratamento


@admin.register(Tratamento)
class TratamentoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "status_tratamento",
        "data_inicio_tratamento",
        "descricao_tratamento",
        "data_fim_tratamento",
    )
    search_fields = (
        "status_tratamento",
        "data_inicio_tratamento",
        "data_fim_tratamento",
    )
