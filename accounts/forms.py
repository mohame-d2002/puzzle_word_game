from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class BaseSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'age', 'email', 'what_do_you_like', 'password1', 'password2']

class SignupMenForm(BaseSignUpForm):
    pass

class SignupWomenForm(BaseSignUpForm):
    pass


class SignupKidsForm(UserCreationForm):
    class Meta:
        model= CustomUser
        fields = ['first_name', 'last_name', 'age', 'school_grade', 'what_do_you_like', 'password1', 'password2']




# LOGIN
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class NameLoginForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=150)
    last_name = forms.CharField(label='Last Name', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(first_name=first_name, last_name=last_name)
        except User.DoesNotExist:
            raise forms.ValidationError("Invalid first name or last name.")

        user = authenticate(email=user.email, password=password)
        if user is None:
            raise forms.ValidationError("Invalid password.")
        cleaned_data['user'] = user
        return cleaned_data
