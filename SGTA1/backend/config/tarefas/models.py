from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    titulo = models.CharField(max_Lenght=255)
    descricao = models.TextField()
    status = models.CharField(max_lenght=20, choices=STATUS_CHOICES, default='ABERTA')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    STATUS_CHOICES = [
        ('ATIVO', 'Ativo'),
        ('INATIVO', 'Inativo'),
    ]
    nome = models.CharField(max_Length=200)
    email = models.EmailField
    ativo = models.BooleanField(max_lenght=20, choices=STATUS_CHOICES, default="ATIVO")
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome