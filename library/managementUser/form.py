from django import forms
from register.models import User
from .models import admin_library
from location.models import library_location

class form_edit_user(forms.ModelForm):
    ACTIVE_CHOICES = [
        (False, "Not Active"),
        (True, 'Active'),
    ]

    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=True,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'is_active']


class AdminLibraryForm(forms.ModelForm):
    decsription = forms.CharField(required=False)

    class Meta:
        model = admin_library
        fields = ['library_location', 'decsription']
