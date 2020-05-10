from rest_framework import serializers
from . models import Contador, Consumo


class ContadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contador
        fields = '__all__'

class ConsumoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consumo
        fields = '__all__'


class ContadorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contador
        fields = ['contrato','modelo', 'fecha_vencimiento']


