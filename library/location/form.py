from django import forms
from .models import library_location


class form_create_loc(forms.ModelForm):
    decsription = forms.CharField(required=False)

    class Meta:
        model = library_location
        fields = ['name', 'city', 'address', 'decsription']

class form_edit_loc(forms.ModelForm):
    ACTIVE_CHOICES = [
        (False, "Not Active"),
        (True, 'Active'),
    ]

    decsription = forms.CharField(required=False)
    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = library_location
        fields = ['name', 'city', 'address', 'decsription', 'is_active']
