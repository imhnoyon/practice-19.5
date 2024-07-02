from django import forms
from . import models
class MusicianForm(forms.ModelForm):
    class Meta:
        model=models.MusicianModel
        fields='__all__'

        