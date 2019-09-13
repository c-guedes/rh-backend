from django.shortcuts import render
from django.views.generic import ListView
from .models import Funcionario,Lotacao,Cargo,EstadoCivil,Municipio,Estados
from .serializers import FuncionarioSerializer,CargoSerializer,LotacaoSerializer,MunicipioSerializer,EstadosSerializer
from rest_framework import generics

# Create your views here.
class FuncionarioList(generics.ListCreateAPIView):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class CargoList(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class LotacaoList(generics.ListCreateAPIView):
    queryset = Lotacao.objects.all()
    serializer_class = LotacaoSerializer

class MunicipioList(generics.ListCreateAPIView):
    queryset = Municipio.objects.all()
    serializer_class = MunicipioSerializer

class EstadosList(generics.ListCreateAPIView):
    queryset = Estados.objects.all()
    serializer_class = EstadosSerializer

class GetFuncionario(generics.ListCreateAPIView):
    serializer_class = FuncionarioSerializer
    def get_queryset(self):
        queryset = Funcionario.objects.filter(pk=self.kwargs['pk'])
        return queryset
