from django.contrib import admin
from .models import Funcionario,Lotacao,Cargo,EstadoCivil,Municipio,Estados,Sexo

@admin.register(Funcionario, Lotacao, Cargo, EstadoCivil, Municipio,Estados, Sexo)
class HelpDesk(admin.ModelAdmin):
    pass

# Register your models here.
