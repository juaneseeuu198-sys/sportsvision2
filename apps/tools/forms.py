from django import forms
from .models import CalculoCaloria


class CaloriasForm(forms.ModelForm):
    class Meta:
        model = CalculoCaloria
        fields = ['genero', 'edad', 'peso', 'altura', 'nivel_actividad', 'objetivo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control sv-input'

        self.fields['genero'].widget = forms.RadioSelect(
            choices=CalculoCaloria.GENERO_CHOICES,
            attrs={'class': 'gender-radio'}
        )


class IMCForm(forms.Form):
    altura = forms.FloatField(
        min_value=50, max_value=300,
        widget=forms.NumberInput(attrs={
            'class': 'form-control sv-input',
            'placeholder': '170',
            'step': '0.1'
        })
    )
    peso = forms.FloatField(
        min_value=10, max_value=500,
        widget=forms.NumberInput(attrs={
            'class': 'form-control sv-input',
            'placeholder': '70',
            'step': '0.1'
        })
    )
