from rest_framework import serializers
from .models import EstadoCivil,Estados,Municipio,Funcionario,Cargo,Lotacao

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        depth = 1
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        depth = 1
        fields = '__all__'

class LotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lotacao
        depth = 1
        fields = '__all__'

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        depth = 1
        fields = '__all__'

class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estados
        depth = 1
        fields = '__all__'