from rest_framework import serializers
from .models import Transformador


class TransformadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transformador
        fields = "__all__"
