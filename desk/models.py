from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
import random
import string

class Lotacao(models.Model):
    lotacao = models.CharField("Lotacao", max_length = 128)
    def __str__(self):
        return self.lotacao

class Cargo(models.Model):
    departamento = models.CharField("Cargo", max_length = 128)
    def __str__(self):
        return self.departamento

class EstadoCivil(models.Model):
    estadoCivil = models.CharField("Estado Civil", max_length = 128)
    def __str__(self):
        return self.estadoCivil

class Sexo(models.Model):
    sexo = models.CharField("Sexo", max_length = 128)
    def __str__(self):
        return self.sexo

class Municipio(models.Model):
    municipio = models.CharField("Municipio", max_length = 128)
    def __str__(self):
        return self.municipio

class Estados(models.Model):
    estado = models.CharField("Estado", max_length = 128)
    def __str__(self):
        return self.estado

class Funcionario(models.Model):
    nome = models.CharField("Nome do Funcionário", max_length = 128)
    data_de_nascimento = models.DateField(
        'Data de nascimento', null=True)
    matricula = models.CharField("Matricula",max_length = 128,primary_key=True,unique=True)
    sexo =  models.ForeignKey(Sexo, verbose_name="Sexo", on_delete=models.CASCADE,blank=False)
    telefone_celular = models.CharField("Telefone celular", max_length=15,
    help_text = 'Número do telefone celular no formato (99) 99999-9999',blank=False,unique=True)
    email = models.EmailField('E-mail',blank=False,unique=True)
    is_editable = models.BooleanField('Editavel?',blank=False)
    lotacao = models.ForeignKey(Lotacao, verbose_name="Departamento que o Funcionario está lotado", on_delete=models.CASCADE,blank=False)
    cargo = models.ForeignKey(Cargo, verbose_name="Cargo do funcionario", on_delete=models.CASCADE,blank=False)
    estadoCivil = models.ForeignKey(EstadoCivil, verbose_name="Estado Civil", on_delete=models.CASCADE,blank=False)
    estadoNascimento = models.ForeignKey(Estados, verbose_name="Estado de nascimento", on_delete=models.CASCADE,blank=False)
    municipioNascimento = models.ForeignKey(Municipio, verbose_name="Municipio de nascimento", on_delete=models.CASCADE,blank=False)

    def __str__(self):
        return self.nome

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_matricula_new_id_id_generator(instance):
    matricula_new_id= random_string_generator()

    Klass= instance.__class__

    qs_exists= Klass.objects.filter(order_id= matricula_new_id).exists()
    if qs_exists:
        return unique_matricula_new_id_id_generator(instance)
    print( matricula_new_id)
    return matricula_new_id

def pre_save_create_unique_matricula(sender, instance, *args, **kwargs):
    if not instance.matricula:
        instance.matricula = unique_matricula_new_id_id_generator(instance)


pre_save.connect(pre_save_create_unique_matricula, sender=Funcionario)




