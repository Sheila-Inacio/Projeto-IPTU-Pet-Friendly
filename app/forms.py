from django.forms import ModelForm
from app.models import Contribuinte
from app.models import Carros
from app.models import Pets

# Create the form class.


class ContriForm(ModelForm):
    class Meta:
        model = Contribuinte
        fields = ['nome_completo', 'cpf',
                  'email', 'telefone',
                  'endereco', 'numero', 'complemento',
                  'bairro', 'cidade', 'estado',
                  'inscricao_municipal', 'indicacao_fiscal']


# Create the form class.
class CarrosForm(ModelForm):
    class Meta:
        model = Carros
        fields = ['modelo', 'marca', 'ano']


class PetsForm(ModelForm):
    class Meta:
        model = Pets
        fields = ['nome', 'raca', 'idade', 'tamanho',
                  'contribuinte', 'numero_identificacao']
