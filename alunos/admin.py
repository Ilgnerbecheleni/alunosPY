from django.contrib import admin
from .models import Aluno, VinculoAlunoResponsavel

class VinculoInline(admin.TabularInline):
    model = VinculoAlunoResponsavel
    extra = 1

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "telefone", "cidade", "escolaridade", "criado_em")
    search_fields = ("nome", "cpf", "telefone", "cidade", "bairro")
    list_filter = ("escolaridade", "cor", "cidade")
    inlines = [VinculoInline]
