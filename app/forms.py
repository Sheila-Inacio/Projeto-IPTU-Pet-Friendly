from django.forms import ModelForm
from app.models import Contribuinte

# Create the form class.


class ContriForm(ModelForm):
    class Meta:
        model = Contribuinte
        fields = ['nome_completo', 'cpf',
                  'email', 'telefone',
                  'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'estado',
                  'inscricao_municipal', 'indicacao_fiscal']
