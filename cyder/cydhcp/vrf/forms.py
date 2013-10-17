from django import forms

from cyder.cydhcp.vrf.models import Vrf, VrfAV
from cyder.base.mixins import UsabilityFormMixin


class VrfForm(forms.ModelForm, UsabilityFormMixin):
    class Meta:
        model = Vrf


class VrfAVForm(forms.ModelForm):
    entity = forms.ModelChoiceField(
        queryset=Vrf.objects.all(),
        widget=forms.HiddenInput())

    class Meta:
        model = VrfAV
        fields = ('entity', 'attribute', 'value')
