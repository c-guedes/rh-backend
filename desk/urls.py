from django.urls import path
from . import views
from django.conf.urls import url
from .models import EstadoCivil,Estados,Municipio,Funcionario,Cargo,Lotacao

urlpatterns = [
    url(r'^funcionarios/$', views.FuncionarioList.as_view(), name='funcionarios-list'),
    url(r'^estados/$', views.EstadosList.as_view(), name='estados-list'),
    url(r'^cargos/$', views.CargoList.as_view(), name='cargos-list'),
    url(r'^lotacao/$', views.LotacaoList.as_view(), name='lotacoes-list'),
    url(r'^municipio/$', views.MunicipioList.as_view(), name='municipio-list'),
    url(r'^funcionario/(?P<pk>[0-9]+)/$', views.GetFuncionario.as_view(), name='funcionario-matricula-detail'),
]
