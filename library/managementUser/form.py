from django import forms
from register.models import User

class form_edit_user(forms.ModelForm):

    ACTIVE_CHOICES = [
        (False, "Not Active"),
        (True, 'Active'),
    ]

    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email','role', 'is_active']
