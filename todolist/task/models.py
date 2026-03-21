from django.db import models

class State(models.TextChoices):
    NOVA = 'nova', 'Nova'
    EM_ANDAMENTO = 'em_andamento', 'Em Andamento'
    CONCLUIDA = 'concluida', 'Concluída'
    CANCELADA = 'cancelada', 'Cancelada'

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    deadline = models.DateField
    completion_date = models.DateField(null=True,blank=True)
    state = models.CharField(choices=State)


