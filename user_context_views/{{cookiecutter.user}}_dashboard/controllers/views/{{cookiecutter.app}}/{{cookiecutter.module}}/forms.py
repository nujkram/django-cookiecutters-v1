from django import forms
from {{ cookiecutter.master_reference_plural }}.models.{{ cookiecutter.master_reference }}.models import {{ cookiecutter.model }}


class {{ cookiecutter.model }}Form(forms.ModelForm):
    class Meta:
        model = {{ cookiecutter.model }}
        fields = '__all__'
