from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from . models import Record

# - Register / Create a user

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



# - Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



# - Create Record Form
class CreateRecordForm(forms.ModelForm):
    class Meta:
        model =  Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'country', 'image_url']


# - Update Record Form
class UpdateRecordForm(forms.ModelForm):
    class Meta:  
        model =  Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'city', 'country', 'image_url']