from django import forms
from contatos.models import Pessoa

class ContatosModel2Form(forms.ModelForm):
    dtNasc = forms.DateField(
        input_formats=['%d/%m/%Y'],
        label='Data de nascimento',
        help_text='Nascimento no formato DD/MM/AAAA'
    )

    class Meta:
        model = Pessoa
        fields = '__all__'
