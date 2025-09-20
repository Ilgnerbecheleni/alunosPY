from django import forms
from .models import Aluno, VinculoAlunoResponsavel
from responsaveis.models import Responsavel
import re
_digits = re.compile(r"\D+")

class AlunoForm(forms.ModelForm):
    responsaveis = forms.ModelMultipleChoiceField(
        queryset=Responsavel.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={"size": 6}),
        help_text="Segure Ctrl (ou Cmd) para selecionar vários.",
    )

    class Meta:
        model = Aluno
        fields = [
            "nome", "telefone", "cpf", "idade",
            "rua", "bairro", "cidade", "cep",
            "cor", "escolaridade",
            "responsaveis",
        ]
        widgets = {
            "idade": forms.NumberInput(attrs={"min": 0, "step": 1, "inputmode": "numeric"}),
            "telefone": forms.TextInput(attrs={"placeholder": "(11) 91234-5678", "inputmode": "tel"}),
            "cpf": forms.TextInput(attrs={"placeholder": "000.000.000-00", "inputmode": "numeric"}),
            "cep": forms.TextInput(attrs={"placeholder": "00000-000", "inputmode": "numeric"}),
        }

    # (seus clean_cpf/cep se já tinha – pode reaproveitar)

    def save(self, commit=True):
        aluno = super().save(commit)
        # Sincroniza vínculos simples (tipo padrão “Responsável Legal”, principal=False)
        responsaveis = self.cleaned_data.get("responsaveis")
        if commit:
            VinculoAlunoResponsavel.objects.filter(aluno=aluno).exclude(responsavel__in=responsaveis).delete()
            for r in (responsaveis or []):
                VinculoAlunoResponsavel.objects.get_or_create(
                    aluno=aluno, responsavel=r,
                    defaults={"tipo": "Responsável Legal", "principal": False}
                )
        return aluno
