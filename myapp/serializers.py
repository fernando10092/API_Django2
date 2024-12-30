from rest_framework import serializers
from .models import Banco

class MySerializer(serializers.Serializer):
    class Meta:
        model = Banco
        fields = '__all__'