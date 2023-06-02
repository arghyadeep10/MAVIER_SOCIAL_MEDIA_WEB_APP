from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, )
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), )
    password1 = forms.CharField(label=('Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}), help_text="""
    <small>
    <ul class="text-muted">
    <li> Your password can’t be too similar to your other personal information. </li>
    <li> Your password must contain at least 8 characters. </li>
    <li> Your password can’t be a commonly used password. </li>
    <li> Your password can’t be entirely numeric. </li>
    </ul>
    </small>
    """)
    password2 = forms.CharField(label=('Confirm Password'), widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}), )
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'textinput textInput form-control', 'placeholder': 'Email'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, )
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, )
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email',]


class ProfileUpdateForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}), max_length=32, )
    country_of_residence = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country of Residence'}), max_length=32, )
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth (in yyyy-mm-dd format)'}))
    # gender = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    # relationship_status = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Relationship Status'}))
    profession = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Profession'}), max_length=32, )
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bio (in 60-70 characters)'}), max_length=70, )

    class Meta:
        model = UserProfile
        fields = ['phone', 'country_of_residence', 'dob', 'gender', 'relationship_status', 'profession', 'bio', 'image' ]
