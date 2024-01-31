from django import forms
from .models import author, genre


class form_create_author(forms.ModelForm):
    first_name = forms.CharField(label= "First Name")
    middle_name = forms.CharField(required=False, label= "Middle Name")
    last_name = forms.CharField(required=False, label= "Last Name")

    class Meta:
        model = author
        fields = ['first_name', 'middle_name', 'last_name']

class form_edit_author(forms.ModelForm):
    ACTIVE_CHOICES = [
        (False, "Not Active"),
        (True, 'Active'),
    ]

    first_name = forms.CharField(label= "First Name")
    middle_name = forms.CharField(required=False, label= "Middle Name")
    last_name = forms.CharField(required=False, label= "Last Name")
    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = author
        fields = ['first_name', 'middle_name', 'last_name', 'is_active']

class form_create_genre(forms.ModelForm):

    class Meta:
        model = genre
        fields = ['name']

class form_edit_genre(forms.ModelForm):
    ACTIVE_CHOICES = [
        (False, "Not Active"),
        (True, 'Active'),
    ]

    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = genre
        fields = ['name', 'is_active']
