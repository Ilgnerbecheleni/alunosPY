from django.contrib import admin
from .models import Responsavel

@admin.register(Responsavel)
class ResponsavelAdmin(admin.ModelAdmin):
    list_display = ("nome", "cpf", "telefone", "cidade", "criado_em")
    search_fields = ("nome", "cpf", "telefone", "cidade")
    list_filter = ("cidade",)
