from django import forms
from .models import Responsavel
import re
_digits = re.compile(r"\D+")

class ResponsavelForm(forms.ModelForm):
    class Meta:
        model = Responsavel
        fields = [
            "nome", "telefone", "cpf", "idade",
            "rua", "bairro", "cidade", "cep",
            "cor", "escolaridade",
        ]
        widgets = {
            "idade": forms.NumberInput(attrs={"min": 0, "step": 1, "inputmode": "numeric"}),
            "telefone": forms.TextInput(attrs={"placeholder": "(11) 91234-5678", "inputmode": "tel"}),
            "cpf": forms.TextInput(attrs={"placeholder": "000.000.000-00", "inputmode": "numeric"}),
            "cep": forms.TextInput(attrs={"placeholder": "00000-000", "inputmode": "numeric"}),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get("cpf")
        if not cpf: return cpf
        digits = _digits.sub("", cpf)
        if len(digits) != 11:
            raise forms.ValidationError("CPF deve ter 11 dígitos.")
        return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"
    def clean_cep(self):
        cep = self.cleaned_data.get("cep")
        if not cep: return cep
        digits = _digits.sub("", cep)
        if len(digits) != 8:
            raise forms.ValidationError("CEP deve ter 8 dígitos.")
        return f"{digits[:5]}-{digits[5:]}"
