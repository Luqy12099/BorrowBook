from django import forms
from .models import author, genre, publisher, book
from location.models import library_location
from managementUser.models import admin_library

#region ================================= AUTHOR AREA ==========================================================================

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
#endregion ================================= AUTHOR AREA ==========================================================================


#region ================================= GENRE AREA ==========================================================================

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
#endregion ================================= GENRE AREA ==========================================================================


#region ================================= PUBLISHER AREA ==========================================================================

class form_create_publisher(forms.ModelForm):

    class Meta:
        model = publisher
        fields = ['name']

class form_edit_publisher(forms.ModelForm):
    ACTIVE_CHOICES = [
        (False, "Not Active"),
        (True, 'Active'),
    ]

    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = publisher
        fields = ['name', 'is_active']
#endregion ================================= PUBLISHER AREA ==========================================================================


#region ================================= BOOK AREA ==========================================================================

class form_create_book(forms.ModelForm):
    tittle = forms.CharField(label= "Tittle")
    author = forms.ModelChoiceField(queryset=author.objects.all(), label="Author")
    genre = forms.ModelChoiceField(queryset=genre.objects.all(), label= "Genre")
    publisher = forms.ModelChoiceField(queryset=publisher.objects.all(), label= "Publisher")
    library_location = forms.ModelChoiceField(queryset=library_location.objects.all(), label= "Library")

    stock = forms.IntegerField(label= "Number of Book")
    total_page = forms.IntegerField(required=False, label= "Total Page")
    isbn = forms.CharField(required=False, label= "ISBN")
    published_date = forms.DateField(required=False, label= "Published Date", widget=forms.DateInput(attrs={'type': 'date'}))

    # python constructor
    def __init__(self, user, *args, **kwargs):
        super(form_create_book, self).__init__(*args, **kwargs)
        
        # Customize the label of each choice in the dropdown
        self.fields['author'].label_from_instance = self.label_from_author_instance

        if user.role == 'admin':
            admin_libraries = admin_library.objects.filter(user=user)
            library_locations = [admin_lib.library_location for admin_lib in admin_libraries]
            self.fields['library_location'].queryset = library_location.objects.filter(name__in=library_locations)

    def label_from_author_instance(self, obj):
        # Customize how each author instance is displayed in the dropdown
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}".strip()

    class Meta:
        model = book
        fields = ['tittle', 'author', 'genre', 'publisher','library_location', 'stock',
                   'total_page', 'isbn', 'published_date']


class form_edit_book(forms.ModelForm):
    ACTIVE_CHOICES = [
        (False, "Not Active"),
        (True, 'Active'),
    ]

    is_active = forms.ChoiceField(choices=ACTIVE_CHOICES, label='Select Activate', required=False,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    
    tittle = forms.CharField(label= "Tittle")
    author = forms.ModelChoiceField(queryset=author.objects.all(), label="Author")
    genre = forms.ModelChoiceField(queryset=genre.objects.all(), label= "Genre")
    publisher = forms.ModelChoiceField(queryset=publisher.objects.all(), label= "Publisher")
    library_location = forms.ModelChoiceField(queryset=library_location.objects.all(), label= "Library")

    stock = forms.IntegerField(label= "Number of Book")
    total_page = forms.IntegerField(required=False, label= "Total Page")
    isbn = forms.CharField(required=False, label= "ISBN")
    published_date = forms.DateField(required=False, label= "Published Date", widget=forms.DateInput(attrs={'type': 'date'}))
    
    # python constructor
    def __init__(self, user, *args, **kwargs):
        super(form_edit_book, self).__init__(*args, **kwargs)
        # Customize the label of each choice in the dropdown
        self.fields['author'].label_from_instance = self.label_from_author_instance

        if user.role == 'admin':
            admin_libraries = admin_library.objects.filter(user=user)
            library_locations = [admin_lib.library_location for admin_lib in admin_libraries]
            self.fields['library_location'].queryset = library_location.objects.filter(name__in=library_locations)

    def label_from_author_instance(self, obj):
        # Customize how each author instance is displayed in the dropdown
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}".strip()
    
    class Meta:
        model = book
        fields = ['tittle', 'author', 'genre', 'publisher','library_location', 'stock',
                   'total_page', 'isbn', 'published_date']
#endregion ================================= BOOK AREA ==========================================================================
