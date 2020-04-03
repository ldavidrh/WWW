from django.shortcuts import render
from .models import Consumo, Contador
from .serializers import ConsumoSerializer, ContadorSerializer, ContadorCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from random import randint, uniform,random



class ListaConsumo(APIView):

    def get(self, request):
        consumos = Consumo.objects.all()
        serializer = ConsumoSerializer(consumos, many=True)
        return Response(serializer.data)

class ListaConsumoCliente(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        consumos = Consumo.objects.filter(contador__contrato__cliente__cedula=id)
        serializer = ConsumoSerializer(consumos, many=True)
        return Response(serializer.data)


class CrearConsumo(APIView):

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        contador = Contador.objects.get(id=id)
        lectura_anterior = Consumo.objects.filter(contador=contador).last()
        ran = randint(200,300)

        if lectura_anterior != None:

            lectura_actual = ran + lectura_anterior.lectura_actual
            consumo = Consumo(contador=contador, lectura_actual=lectura_actual, lectura_anterior=lectura_anterior.lectura_actual)
            consumo.save()

        else:
            consumo = Consumo(contador=contador, lectura_actual=ran, lectura_anterior=0)
            consumo.save()



        c = Consumo.objects.filter(contador=contador).last()
        print(c)
        serializer = ConsumoSerializer(c)

        
        return Response(serializer.data)



