from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Banco
from .serializers import MySerializer

@api_view(['GET', 'POST'])
def hello_world(request):
    #METODO POST
    if request.method == 'POST':
        return Response({"nome": "Felipe", "idade": 20})
    
    #METODO GET
    Dados_Banco = Banco.objects.all()
    Dados_Serializers = MySerializer(Dados_Banco, many=True)
    return Response(Dados_Serializers.data)