from django.forms import ModelForm
from main.models import Kartu

class KartuForm(ModelForm):
    class Meta:
        model = Kartu
        fields = ['nama_pengirim', 'pesan', 'wish']