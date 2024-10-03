from django.forms import ModelForm
from commune.models import Reclamation

class ReclamationForm(ModelForm):
    class Meta:
        model = Reclamation
        fields = ['nom','numTel','email','sujet','adresseGoogle','photo']