from rest_framework.viewsets import ModelViewSet

from .models import Tratamento
from .serializers import TratamentoSerializer


class TratamentoViewSet(ModelViewSet):
    queryset = Tratamento.objects.all()
    serializer_class = TratamentoSerializer