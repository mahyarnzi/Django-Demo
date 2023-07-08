from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    date = forms.DateField(input_formats=['%d/%m/%Y'])
    table = forms.IntegerField(required=False)

    class Meta:
        model = Reservation
        fields = '__all__'
        # exclude = ['table','status']
