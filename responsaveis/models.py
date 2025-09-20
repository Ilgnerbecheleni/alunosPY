from django.db import models

COR_CHOICES = [
    ("Branca", "Branca"),
    ("Preta", "Preta"),
    ("Parda", "Parda"),
    ("Amarela", "Amarela"),
    ("Indígena", "Indígena"),
    ("Outra", "Outra"),
]

ESCOLARIDADE_CHOICES = [
    ("Infantil", "Educação Infantil"),
    ("Fundamental I", "Fundamental I (1º-5º)"),
    ("Fundamental II", "Fundamental II (6º-9º)"),
    ("Médio", "Ensino Médio"),
    ("Técnico", "Técnico"),
    ("Superior", "Superior"),
    ("EJA", "EJA"),
    ("Outro", "Outro"),
]

class Responsavel(models.Model):
    nome      = models.CharField(max_length=120)
    telefone  = models.CharField(max_length=20, blank=True, null=True)
    cpf       = models.CharField(max_length=14, blank=True, null=True)
    idade     = models.PositiveIntegerField(blank=True, null=True)

    rua       = models.CharField(max_length=200, blank=True, null=True)
    bairro    = models.CharField(max_length=120, blank=True, null=True)
    cidade    = models.CharField(max_length=120, blank=True, null=True)
    cep       = models.CharField(max_length=9, blank=True, null=True)

    cor            = models.CharField(max_length=20, choices=COR_CHOICES, blank=True, null=True)
    escolaridade   = models.CharField(max_length=20, choices=ESCOLARIDADE_CHOICES, blank=True, null=True)

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome
