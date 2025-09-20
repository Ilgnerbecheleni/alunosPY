from django.db import models
from responsaveis.models import Responsavel  # <- importe o model
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

class Aluno(models.Model):
    # (seus campos existentes)
    nome  = models.CharField(max_length=120)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    cpf   = models.CharField(max_length=14, blank=True, null=True)
    idade = models.PositiveIntegerField(blank=True, null=True)

    rua   = models.CharField(max_length=200, blank=True, null=True)
    bairro = models.CharField(max_length=120, blank=True, null=True)
    cidade = models.CharField(max_length=120, blank=True, null=True)
    cep   = models.CharField(max_length=9, blank=True, null=True)

    cor = models.CharField(max_length=20, blank=True, null=True)
    escolaridade = models.CharField(max_length=20, blank=True, null=True)

    # >>> RELACIONAMENTO
    responsaveis = models.ManyToManyField(
        Responsavel,
        through='VinculoAlunoResponsavel',
        related_name='alunos',
        blank=True,
    )

    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome


TIPO_VINCULO = [
    ("Pai", "Pai"),
    ("Mãe", "Mãe"),
    ("Responsável Legal", "Responsável Legal"),
    ("Outro", "Outro"),
]

class VinculoAlunoResponsavel(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Responsavel, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_VINCULO, default="Responsável Legal")
    principal = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("aluno", "responsavel")  # evita duplicidade
        verbose_name = "Vínculo aluno-responsável"
        verbose_name_plural = "Vínculos aluno-responsável"

    def __str__(self):
        return f"{self.aluno} ⇄ {self.responsavel} ({self.tipo})"
