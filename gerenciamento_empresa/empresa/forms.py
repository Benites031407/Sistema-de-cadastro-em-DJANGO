from django import forms
from .models import Meta

class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta
        fields = ['nome', 'descricao', 'valor', 'data_inicio', 'data_fim', 'setor']